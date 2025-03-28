from langchain.globals import set_llm_cache
from langchain_community.cache import InMemoryCache
set_llm_cache(InMemoryCache())
import time
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(
    temperature=0.95,
    model="glm-4-flash",
    openai_api_key=os.getenv("ZHIPUAI_API_KEY"),
    openai_api_base=os.getenv("ZHIPUAI_URL")
)
prompt = ChatPromptTemplate.from_template('{string}')
chain = prompt | llm|StrOutputParser()
begin = time.time()
print( chain.invoke({'string':'鸡兔同笼问题'}) )
print(f'第一次使用时间:{time.time() - begin }')
begin = time.time()
print( chain.invoke({'string':'鸡兔同笼问题'}) )
print(f'第二次使用时间:{time.time() - begin }')