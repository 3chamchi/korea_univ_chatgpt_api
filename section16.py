# Section 16
# 오디오 변환 프로젝트

# 1. API 연동 준비
import openai

openai.api_key = "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"

# 2. 오디오 파일 읽기
# file_name = '애국가 제창(1절).mp3'
file_name = '짧은 대화의 응답_22006-0337_통파일.mp3'  # 파일 이름 변수, 확장자 포함
audio_file = open(f'media/{file_name}', 'rb')  # 파일 열기

# 3. API 요청
response = openai.Audio.transcribe("whisper-1", audio_file)  # API 요청

# 4. API 요청 응답 확인
print(response)
print(response['text'])
