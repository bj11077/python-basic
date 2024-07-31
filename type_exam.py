# 변수의 type을 확인할때 사용
number= 6
print(type(number))

# float
float_num = 5 / 3
print(type(float_num))

# 복소수
# complex
comp=3+4j
print(comp)
print(type(comp))
#허수 및 제곱
(1j) **2
# 10제곱
(1+1j) **10


# 문자열 = list = tuple  이것들은 시퀀스에 속함
type("Love your Enemies, for they tell you your Faults.")
#<class 'str'>
type(['love', 'enemy', 'fault'])
#<class 'list'>
type(('love', 'enemy', 'fault'))
#<class 'tuple'>


#매핑 dict타입  key : value
print(type({'one':1,'two':2}))

# set 타입   -  집합을 표현함
fruits = {'apple','banana','orange'}
print(fruits)