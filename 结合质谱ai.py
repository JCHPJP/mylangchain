from langchain.llms.base import LLM
from zhipuai import ZhipuAI
from langchain_core.messages.ai import AIMessage
import os
from dotenv import load_dotenv
load_dotenv()
class ChatGLM_4_flash(LLM):
    client:object = None
    def __init__(self):
        super().__init__()
        self.client = ZhipuAI( api_key = os.getenv('ZHIPUAI_API_KEY') )


    def _llm_type(self) -> str:
        return 'GLM-4-Flash'
    def invoke(self,prompt,history= []):
        if history is None:
            history = []
        history.append({'role':'user','content':prompt})
        responses = self.client.chat.completions.create(
            model='glm-4-flash',
            messages= history,
            stream = False
        )
        result = responses.choices[0].message.content
        return AIMessage(result)
    def _call(self,prompt,history= []):
        return self.invoke(prompt,history)
    def stream(self,prompt,history= []):
        if history is None:
            history = []
        history.append({'role':'user','content':prompt})
        response = self.client.chat.completions.create(
            model='glm-4-flash',
            messages=history,
            stream = True
        )
        for chunk in response:
            yield chunk.choices[0].delta.content
llm = ChatGLM_4_flash()
history =[]
# print( llm.invoke('').content ) # 非流式调用
for i in llm.stream('RAG的技术有哪些？什么是RAG？'):
    print(i,end='')


