import os
from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage , HumanMessage , AIMessage
llm = ChatOpenAI(
    temperature=0.95,
    model="glm-4-flash",
    openai_api_key=os.getenv("ZHIPUAI_API_KEY"),
    openai_api_base="https://open.bigmodel.cn/api/paas/v4/"
)

prompt = ChatPromptTemplate.from_messages([
    "你是智能助手",
    HumanMessage(content="早餐有什么推荐")
])

input_data = {}

print(prompt)
# 创建链
chain = prompt | llm |StrOutputParser()

# 调用链
result = chain.invoke(input_data)
print(type(result) , result)

