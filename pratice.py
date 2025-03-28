import os
from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_template('你能使用{name}吗')
prompt_value = prompt.invoke({'name':'gpt'})
print(prompt_value )
model = ChatOpenAI(model='' ,api_key=os.getenv('key'))
model.invoke(prompt_value)
output_parser = StrOutputParser()
chains = prompt | model | output_parser
