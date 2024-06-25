# 如何使用azure OpenAI
要使用Azure OpenAI服务，您需要完成以下几个步骤，包括申请访问权限、创建和部署资源，以及进行简单的API调用。以下是一个最简单的申请和部署的例子：

## 1. 申请访问权限

首先，您需要申请对Azure OpenAI服务的访问权限。可以通过以下步骤完成：

1. 访问[Azure OpenAI访问申请页面](https://aka.ms/oai/access)。
2. 填写表单，确保使用企业邮箱和真实的企业信息。
3. 提交申请后，等待审核通过。审核时间可能从几小时到几天不等。

## 2. 创建Azure OpenAI资源

审核通过后，您可以在Azure门户中创建OpenAI资源：

1. 登录到[Azure门户](https://portal.azure.com/)。
2. 点击“创建资源”，搜索“Azure OpenAI”，然后选择“创建”。
3. 在“创建Azure OpenAI”页面上，填写以下信息：
   - **订阅**：选择您的Azure订阅。
   - **资源组**：选择现有资源组或创建新资源组。
   - **区域**：选择资源的部署区域。
   - **名称**：为资源命名，例如“MyOpenAIResource”。
   - **定价层**：选择标准层。
4. 点击“查看+创建”，然后点击“创建”。

## 3. 部署模型

创建资源后，您需要部署一个模型：

1. 登录到[Azure OpenAI Studio](https://oai.azure.com/)。
2. 选择您的订阅和Azure OpenAI资源，然后点击“使用资源”。
3. 在“管理”下，选择“部署”。
4. 点击“创建新部署”，并配置以下字段：
   - **选择模型**：选择您需要的模型，例如`gpt-35-turbo`。
   - **部署名称**：为部署命名，例如“MyDeployment”。
5. 点击“创建”，等待部署完成。

## 4. 获取API密钥和终结点

部署完成后，您需要获取API密钥和终结点以进行API调用：

1. 在Azure门户中，导航到您的Azure OpenAI资源。
2. 在“密钥和终结点”部分，复制API密钥和终结点URL。

## 5. 进行简单的API调用

以下是一个使用Python进行简单API调用的示例：

```python
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

```

在上述代码中，替换`YOUR_API_KEY`和`YOUR_ENDPOINT`为您从Azure门户获取的实际值。

通过以上步骤，您可以成功申请和部署Azure OpenAI服务，并进行简单的API调用。更多详细信息可以参考[Azure OpenAI文档](https://learn.microsoft.com/zh-cn/azure/ai-services/openai/quickstart)[1][2][3]。

Citations:
[1] https://learn.microsoft.com/zh-cn/azure/ai-services/openai/quickstart
[2] https://learn.microsoft.com/zh-cn/azure/ai-services/openai/how-to/create-resource
[3] https://51.ruyo.net/18402.html
[4] https://learn.microsoft.com/zh-cn/training/paths/develop-ai-solutions-azure-openai/
[5] https://learn.microsoft.com/zh-tw/azure/ai-services/openai/quickstart
[6] https://www.wangwangit.com/Azure%20OpenAI%20%E7%94%B3%E8%AF%B7%E4%B8%8E%E4%BD%BF%E7%94%A8%E8%AF%A6%E7%BB%86%E6%95%99%E7%A8%8B/
[7] https://www.cnblogs.com/stulzq/p/17271937.html
[8] https://learn.microsoft.com/zh-cn/azure/ai-services/openai/use-your-data-quickstart
[9] https://learn.microsoft.com/zh-cn/azure/ai-services/openai/
[10] https://blog.csdn.net/m0_71858447/article/details/135656444