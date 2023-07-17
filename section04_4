# Section04 - 4
#4 업다운 게임

# 1~100까지 랜덤한 값을 맞추는 게임
# 입력한 값이 랜덤값 보다 낮은 경우 다운, 높은 경우 업, 같은 경우 정답 출력
# 입력값 : 예측 정답값
# 출력 값 : 업, 다운, 정답

# 1. 랜덤한 정답 생성
import random
answer = random.randint(1, 100)

while True:
    # 2. 예측 답을 입력
    num = input('예상 답을 입력해주세요 : ')
    num = int(num)

    # 3. 정답 확인
    if num == answer:
        print('정답')
        break
    elif num > answer:
        print('다운')
    else:
        print('업')

# 4. 결과 출력
