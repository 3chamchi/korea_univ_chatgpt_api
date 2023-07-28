# Section04 - 10
# 10 별찍기 마름모

print('''마름모 별찍기 프로그램
예시) 5을 입력할 경우 ================
    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *
==================================''')
line_num = input('출력할 줄 수를 입력해주세요 : ')
line_num = int(line_num)

for i in range(1, line_num + 1):
    for j in range(line_num - i):
        print(' ', end='')
    for j in range(1, i * 2, 1):
        print('*', end='')
    print('')
for i in range(line_num):
    for j in range(i):
        print(' ', end='')
    for j in range(line_num * 2, 1 + i * 2, -1):
        print('*', end='')
    print('')
