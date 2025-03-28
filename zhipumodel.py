import os
from dotenv import load_dotenv
from zhipuai import ZhipuAI
load_dotenv()
client = ZhipuAI(api_key=os.getenv('ZHIPUAI_API_KEY'))
from openai import OpenAI
# # 流式输出
# prompt = '最近国际发生了什么大事？'
# responses = client.chat.completions.create(
#     model='glm-4-flash',
#     messages=[
#         {'role':'system',"content":'我是国际大事观察者'},
#         {'role':'user','content':prompt}
#     ],
#     stream = True
# )
# for response in responses:
#     print(response.choices[0].delta.content,end= '')
# 非流式输出
prompt = '介绍一下yield关键字，举一下例子'
responses = client.chat.completions.create(
    model='glm-4-flash',
    messages=[
        {'role':'system',"content":'AI助手'},
        {'role':'user','content':prompt}
    ],
    stream = False
)
print(responses.choices[0].message.content)


