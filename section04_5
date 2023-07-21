# Section04 - 5
# 6 별찍기

# 입력값 : 출력하고자 하는 줄 수 입력
# 출력 값 : N개의 줄에 N개의 별(*) 출력, 강의안 참고

print('''별찍기 프로그램
예시) 3을 입력할 경우
*
**
***''')
line_num = input('출력할 줄 수를 입력해주세요 : ')
line_num = int(line_num)

# 일반적 별찍기, 중첩 포문
print('Case 1')
for i in range(line_num):  # 줄찍기 역할 : 입력 받은 줄 수만큼 반복
    for j in range(i + 1):  # 별찍기 역할 : 줄 수 만큼 * 출력
        print('*', end='')  # print() * 출력 end=''로 줄바꿈 제거
    print()  # 줄바꿈을 위한 print()

# 파이썬스럽게
print('\nCase 2')  # 문자열 출력시 \n는 줄바꿈을 의미
for index in range(1, line_num + 1):
    print('*' * index)  # '*' * index를 통해 줄수 만큼 연산하여 출력
