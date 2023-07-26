# Section 11
# 번역기 만들기
import requests

# 1. API 연동을 위한 준비
chatgpt_api_key = "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"

# 2. ChatGPT API 요청
url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {chatgpt_api_key}",
}

input_text = input("번역할 내용을 입력해주세요 : ")
data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {
            "role": "user",
            "content": input_text + "를 영어로 번역해줘"
        }
    ]
}

response = requests.post(url, headers=headers, json=data)

# 3. 응답 값 출력
print(response.json())
