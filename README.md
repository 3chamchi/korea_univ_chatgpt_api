# korea_univ_chatgpt_api
고려대 세종캠퍼스 ChatGPT API 교육과정

## 목표
- 창업자 및 비전공자를 대상으로 프로그래밍 기초 지식 습득
- Python을 이용한 기본 개발 능력 향상
- ChatGPT API를 활용한 다양한 프로젝트 개발 경험
- 창업 아이디어와 비즈니스에 AI 활용 능력 강화

## 특징
- 프로그래밍 학습 보단 ChatGPT API 사용을 중심으로 서비스 개발에 집중한 교육으로 실습 위주로 진행
- 예제 프로젝트를 진행하며 Python, API, ChatGPT의 역량 강화 및 숙력도 향상

## 커리큘럼
- [x]  1강. 프로그래밍, 파이썬 소개 및 기초 문법
- [x]  2강. 파이썬 자료구조, 함수
- [x]  3강. 파이썬 실습
- [x]  4강. ChatGPT API 기초 및 ChatGPT API 연동
- [x]  5강. ChatGPT API 활용 - 언어 번역기, 이미지 생성기 프로젝트
- [x]  6강. ChatGPT API 활용 - 이미지 생성기 응용, 인터뷰 질문지 제작 프로젝트
- [x]  7강. ChatGPT API 활용 - 상품/서비스 설명 생성기 프로젝트
- [x]  8강. ChatGPT API 활용 - 감정 분석 프로젝트
- [ ]  9강. ChatGPT API 활용 - 아이디어 브레인스토밍 도우미 프로젝트
- [ ] 10강. 최종 프로젝트 및 발표 

## 참고 링크
* 파이썬 무료 책 : https://wikidocs.net/book/1
* OpenAI Developers(ChatGPT API) :  https://platform.openai.com/
* ChatGPT API 적용 사례 : https://openai.com/customer-stories

# 설정 및 명령어
## 설정
#### 파이참 인터프리터(가상환경) 설정
* 파일 -> 설정 -> 프로젝트 폴더 -> Python 인터프리터 -> Python 인터프리터 설정
* 프로젝트 디렉토리에 있는 ```venv```안의 ```python``` 선택
* 없는 경우 가상환경 생성 후 선택

#### 윈도우 가상환경 접속 오류
1. powershell 관리자 권한 실행
2. 명령어 입력 ```Set-ExecutionPolicy Unrestricted```
3. 파이참, 파워쉘 재실행

#### 윈도우 파이참, 파워쉘 연결
1. 파일 -> 설정 -> 도구 -> 터미널 -> 애플리케이션 설정 -> 쉘 경로 -> powershell.exe 선택

## 명령어
### 파이썬

#### 가상환경 생성
* ```python -m venv venv```
* ```python -m venv <가상환경명>```

#### 가상환경 접속  
* 가상환경 접속 시 가상환경 폴더가 있는 위치에서 실행
* 가상환경 접속 후 ```(venv)``` 가상환경명을 접속 확인
* (Windows) ```.\venv\Scrips\activate```
* (Mac) ```soruce venv/bin/activate```

#### 패키지 설치
* ```python -m pip install <패키지명>```
* ```pip install <패키지명>```
  * 교육 중 사용하는 패키지 : ```reqeusts```, ```openai```
  * ```pip install reqeusts``` 
  * ```pip install openai``` 

#### 패키지 확인
* ```pip list```

#### 패키지 업데이트
* ```pip install --upgrade <패키지명>```
* ```pip install --upgrade pip```

### 윈도우 파워쉘, 터미널 명령어
#### 디렉토리(폴더) 이동
* ```cd <디렉토리명>```

#### 현재 경로 확인
* ```pwd```

#### 현재 디렉토리 파일 등 확인
* ```ls```
