# Section04 - 7
# 구구단 찍기
# 구구단을 출력하는 프로그램 작성
# 단을 입력 받아 x9까지 구구단 출력
# 입력값:단수
#  출력 값 : 입력한 단수(x)의 x * 1 ... x *9 값 출력(예시 참고)

# 1. 단을 입력 받는다
dan = input('출력할 단을 입력해주세요 : ')
dan = int(dan)

# 2. 입력 받은 단의 *1부터 *9까지 출력
for index in range(10):  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    if index != 0:
        print(f'{dan} * {index} = {dan * index}')
