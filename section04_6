# Section04 - 6
# 6 별찍기

# 입력값 : 출력하고자 하는 줄 수 입력
# 출력 값 : N개의 줄에 N개의 별(*) 출력, 강의안 참고

print('''별찍기 프로그램
예시) 3을 입력할 경우 ================
Case 1 | Case 2 | Case 3 | Case 4
*      | ***    |      * |    ***
**     | **     |     ** |     **
***    | *      |    *** |      *
==================================''')
line_num = input('출력할 줄 수를 입력해주세요 : ')
line_num = int(line_num)

# *
# **
# ***
print('Case 1')
for i in range(line_num):
    for j in range(i + 1):
        print('*', end='')
    print()

# ***
# **
# *
print('Case 2')
for i in range(line_num, 0, -1):
    for j in range(i):
        print('*', end='')
    print('')

#   *
#  **
# ***
print('Case 3')
for i in range(line_num):
    for j in range(i):
        print(' ', end='')
    for j in range(line_num - i):
        print('*', end="")
    print('')

# ***
#  **
#   *
print('Case 4')
for i in range(1, line_num + 1):
    for j in range(line_num - i):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print('')
