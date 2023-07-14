# Section 03
# 반복문 while, for

var_list = ['빨강', '초록', '파랑', '검정']
print(var_list)
print(var_list[0])
print(var_list[1])
print(var_list[2])
print(var_list[3])

print('==============')
for color in var_list:
    print(color)

index = 0
while True:
    print('Run while...')
    if index > 100:
        break
    index = index + 1
