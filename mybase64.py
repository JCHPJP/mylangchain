import base64
import requests
import os
from dotenv import load_dotenv
load_dotenv()
import base64
from zhipuai import ZhipuAI

img_path = "imgs/img4.png"
with open(img_path, 'rb') as img_file:
    img_base = base64.b64encode(img_file.read()).decode('utf-8')

client = ZhipuAI(api_key=os.getenv('ZHIPUAI_API_KEY')) # 填写您自己的APIKey
response = client.chat.completions.create(
    model="glm-4-flash",  # 填写需要调用的模型名称
    messages=[
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "调用词向量模型需要收api的费用吗？"
          }
        ]
      }
    ]
)
print(response.choices[0].message.content)