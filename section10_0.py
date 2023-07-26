# Section 10 - 0
# ChatGPT API 연동 복습

# 가상환경 접속 방법
## 주의사항 : 가상환경이 있는 폴더 경로에서 입력해야함
# 윈도우 : venv\Scripts\activate
##  * \는 엔터 위에 원화 표시
# 맥 : source venv/bin/activate

# 1. API 연동 준비
# 1-1. 패키지 불러오기
import requests  # pip install requests

# 1-2. url 경로 확인
# API 문서에서 확인
url = 'https://api.openai.com/v1/chat/completions'
# 1-3. 요청 데이터 만들기
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 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'
}
data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Hello!"
        }
    ]
}
# 2. API 요청
response = requests.post(url, headers=headers, json=data)

# 3. 응답 값 사용
print(response.json())
