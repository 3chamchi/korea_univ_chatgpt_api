print('2주차 시작')

# 변수, 자료형
# int 정수
# float 실수
# str 문자열
# list 리스트
# tuple 튜플
# dict 딕셔너리(사전)

var = 2023

var_int = 3
var_float = 3.0
print(var_int)
print(var_float)
print(type(var_int))
print(type(var_float))

var_str1 = 'chatGPT'
var_str2 = "chatGPT"
var_str3 = '''chat
GPT'''
var_str4 = """chat
GPT"""
print(var_str1)
print(var_str2)
print(var_str3)
print(var_str4)
print(type(var_str1))
print(type(var_str2))
print(type(var_str3))
print(type(var_str4))

var_list1 = ['빨강', '초록', '파랑']
var_list2 = []
var_list3 = list()
var_tuple1 = ('빨강', '초록', '파랑')
var_tuple2 = ()
var_tuple3 = tuple()
var_dict1 = {'red': '빨강', 'green': '초록', 'blue': '파랑'}
var_dict2 = {}
var_dict3 = dict()
print(var_list1)
print(var_list2)
print(var_list3)
print(var_tuple1)
print(var_tuple2)
print(var_tuple3)
print(var_dict1)
print(var_dict2)
print(var_dict3)
print(type(var_list1))
print(type(var_list2))
print(type(var_list3))
print(type(var_tuple1))
print(type(var_tuple2))
print(type(var_tuple3))
print(type(var_dict1))
print(type(var_dict2))
print(type(var_dict3))

print(var_list1[0])
print(var_tuple1[0])
# print(var_dict1[0])

print(var_list1[2])
print(var_tuple1[1])

print(var_list1)
var_list1 = var_list1 + [3, 3.0]
print(var_list1)

print(var_dict1['rad'])
print(var_dict1['blue'])
print(var_dict1)
# var_dict1 = {0: '첫 번째'}
# print(var_dict1)
var_dict1[0] = '첫 번째'
print(var_dict1)
item = [
    {
        'name': '콜라',
        'price': 1800
    },
    {
        'name': '물',
        'price': 800
    }
]

print(3 + 2)
print(1 - 1)
print(3 + 2.0)
print(9 / 9)
print(9 * 9)
print(22 // 4)
print(22 % 4)
print(9 ** 9)


var_text1 = '텍스트 중요'
#            0 123
var_text2 = 'ChatGPT API'
print(var_text1)
print(var_text2)

print(var_text1[0])
print(var_text1[1])
print(var_text1[2])
print(var_text1[0:3])
print(var_text1[-2:])
print('20230708-3'[-1])

print('1' + '2' + '3')
print('1', '2', '3')

print(f'var_text1 = {var_text1}')
