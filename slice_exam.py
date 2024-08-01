#문자열 슬라이싱
str_ex01 = 'Python'

# Py
print(str_ex01[0:2])

#문자열 붙이기
str_ex02 = 'hello world!'
attached_str=str_ex02[:6] + str_ex01 +'!'
print(attached_str) # hello Python!

#문자열 뒷부분 숫자늘리면 뒤에서 몇개 이렇게하는거
print(str_ex01[-1:]) # n

#역순으로 다구하기
print(str_ex01[::-1]) # nohtyP

### 위내용 리스트도 동일하게 적용가능 ###

