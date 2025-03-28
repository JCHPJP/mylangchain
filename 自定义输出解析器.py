from langchain_core.messages import AIMessage ,SystemMessage ,HumanMessage
import os
from dotenv import load_dotenv
load_dotenv()
import json

from langchain_openai import ChatOpenAI
llm = ChatOpenAI(
    temperature=0.95,
    model="glm-4-flash",
    openai_api_key=os.getenv("ZHIPUAI_API_KEY"),
    openai_api_base=os.getenv("ZHIPUAI_URL")
)

def parser(ai_message:AIMessage)->map:
    idx = ai_message.content.find('json')
    content = ai_message.content[idx-3:]
    content = content.replace('json','')
    print(content)
    return json.loads( content )

chain = llm
print(llm.invoke('你给我json的数据').content)
from langchain_text_splitters import MarkdownHeaderTextSplitter
headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]

markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on)
md_header_splits = markdown_splitter.split_text(markdown_document)
md_header_splits