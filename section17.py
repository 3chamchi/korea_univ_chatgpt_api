# Section 17
# 감성 분석기 프로젝트

# 1. API 연동 준비
import openai

openai.api_key = "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"

messages = [  # 메시지 리스트 변수
    {
        'role': 'system',
        'content': 'You will be provided with a tweet, and your task is to classify its sentiment as positive, neutral, or negative.'
    }
]

print('==============================================')
print('==============================================')
print('===================감정 분석기===================')
print('텍스트를 입력하면 긍정, 중립, 부적의 감정 분석 결과가 나옵니다.')

while True:
    # 2. 사용자 메시지 생성
    input_text = input('분석할 내용을 입력해주세요 >>> ')  # 사용자 입력
    user_message = {'role': 'user', 'content': input_text}  # 사용자 입력 메시지 변수
    messages.append(user_message)  # 사용자 메시지 추가

    # 3. API 요청
    response = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=messages)  # API 요청, ChatGPT 응답

    # 4. API 응답 확인
    assistant_messages = response.choices[0].message.to_dict()  # ChatGPT assistant 메시지 변수
    messages.append(assistant_messages)

    print(f'> {user_message["role"]} : {user_message["content"]}')
    print(f'> {assistant_messages["role"]} : {assistant_messages["content"]}')

    print('''\n원하는 동작을 입력해주세요.\n1. 계속하기\n2. 주고 받은 메세지 출력 후 종료''')
    action = input('동작 입력 >>> ')

    if action == '2':
        for message in messages:
            print(f'{message["role"]} : {message["content"]}')
        break
    print()

print('==============================================')
print('==============================================')
print('======= 감정 분석기를 이용해주셔서 감사합니다 :) =======')
print('==============================================')
print('==============================================')
