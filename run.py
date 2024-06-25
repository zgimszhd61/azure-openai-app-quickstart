import os
from dotenv import load_dotenv
from openai import AzureOpenAI
load_dotenv()



client = AzureOpenAI(
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
  api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
  api_version="2024-02-01"
)

# 发送请求
response = client.chat.completions.create(
    model = "helloworld",
    messages=[
        {
            'role': 'system',
            "content": "你是一个有帮助的助手，你始终用中文回答问题，不要用英文。"
        },
        {
            'role': 'user',
            "content": "who are you",
        },
    ]
)

# 获取并打印结果
result = response.choices[0].message.content

print(result)
