# Section 02
# 조건문

a = 'ABCD'
if a == 'ABC':
    print('ABC')
else:
    print('...')

number = 79
if number > 90:
    print('A')
    print()
elif number > 80:
    print('B')
else:
    print('F')

print(90 > 80)
print(88 > 90)
number2 = 82
print(90 > number2 and number2 > 80)
print(90 > number2 or 8 > 80)
