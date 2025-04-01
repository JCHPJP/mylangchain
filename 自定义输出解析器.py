from langchain_core.messages import AIMessage ,SystemMessage ,HumanMessage
import os
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
import pandas as pd

load_dotenv()
filenames = [  i for i in os.listdir('./') if '.md' in i ]
print(filenames)

from langchain_text_splitters import MarkdownHeaderTextSplitter
headers_to_split_on = [
    ("#", "Header")
]
with open("01_“未来校园”智能应用专项赛.md",'r',encoding='utf-8') as file :
    markdown_document = file.read()
markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on,strip_headers=False)
md_header_splits = markdown_splitter.split_text(markdown_document)
ans = 0
text = ''
for md_header_split in md_header_splits:
    ans += len(md_header_split.page_content)
    text +=md_header_split.page_content+'\n'
# print(text)
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(
    temperature=0,
    model="glm-4-flash",
    openai_api_key=os.getenv("ZHIPUAI_API_KEY"),
    openai_api_base=os.getenv("ZHIPUAI_URL")
)
# from langchain_deepseek import ChatDeepSeek
# llm = ChatDeepSeek(
#     model='deepseek-chat',
#     temperature=0,
#     max_tokens=None,
#     timeout=None,
#     max_retries=2,
# )
parser = JsonOutputParser()
with open('a.json','r',encoding='utf-8') as file:
    data = file.read()

messages = [SystemMessage('你是一个智能助手'),
           HumanMessage(f'{text}这次内容的赛项名称 赛道 发布时间 报名时间 组织单位 官网 '),
           AIMessage(f'{data}')
           ]
with open("02_3D编程模型创新设计专项赛.md",'r',encoding='utf-8') as file :
    markdown_document = file.read()
markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on,strip_headers=False)
md_header_splits = markdown_splitter.split_text(markdown_document)
ans = 0
text = ''
for md_header_split in md_header_splits:
    ans += len(md_header_split.page_content)
    text +=md_header_split.page_content+'\n'
# print(text)
s = f'{text} 回答 赛项名称 赛道 发布时间 报名时间 组织单位 官网 {parser.get_format_instructions()}'
chain = llm | parser
# reslut = []
# data = pd.DataFrame(reslut)
# data.to_excel('data.xlsx',index = False )
messages.append(HumanMessage(s))
print(len(messages) )
content = chain.invoke(messages)
print(content )


# prompt = PromptTemplate(
#     template="Answer the user query.\n{format_instructions}\n{query}\n",
#     input_variables=["query"],
#     partial_variables={"format_instructions": parser.get_format_instructions()},
# )
# print(parser.get_format_instructions())
# chain = prompt | model | parser
# print( prompt.invoke( '给我一点数据') )
# chain.invoke({"query": joke_query})


