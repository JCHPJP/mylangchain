from dotenv import load_dotenv
import os
load_dotenv()
from openai import OpenAI
client = OpenAI(api_key=os.getenv('deepseek'), base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "你是谁？"},
    ],
    stream=False
)

print(response.choices[0].message.content)