# Section 10
# ChatGPT API 연동
import requests

# 1. API 연동을 위한 준비

# 1-1. API 연동을 위한 요청 패키지 설치.  pip install requests
# 1-2. ChatGPT API 키 가져오기
chatgpt_api_key = "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"

# 2. ChatGPT API 요청
url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {chatgpt_api_key}"
}

data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {
            "role": "user",
            "content": "반가워 chatGPT"
        }
    ]
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
