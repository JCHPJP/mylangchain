from langchain.prompts import PromptTemplate
from datetime import datetime
prompt = PromptTemplate.from_template('{foo}{read}')
print(prompt)
prompt1 = prompt.partial(read='hello world ')
print(prompt1.format() )
prompt2 = prompt1.partial(foo='hello world ')
print( prompt2.format() )