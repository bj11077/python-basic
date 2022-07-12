#  4.4 (찐나누기)
from functools import reduce
from posixpath import split


print(4400 / 1000)

# 400  (나머지)
print(4400 % 1000)  

# 4  나누기후 소수점버림
print(4400 // 1000)

# list
family = ['a','b','c']

#list length
len(family) # 3

#list remove
family.remove('c')

#list append
family.append('e')

print(family)  # ['a','b']



#while
num = 5
while num <= 10:
    print(num)      # 5 6 7 8 9 10
    num += 1

#while문 탈출
while1 = 100
while True:
    if (while1 != 100):
        print('break')
        break;
    else:
        while1 -= 1


#for문
for1 = ['ab','cd','ef']
for x in for1:
    print(x)  # ab cd ef



# round(대상, 반올림할자리수)
print(round(1.235,2))  # 1.24


# if문

if1 = 100

if if1 == 100:
    print('if1 == 100')
elif if1 != 100:
    print('if1 != 100')
else:
    print('else')


# range(시작값, 끝값)  = 시작값 ~ 끝값-1 까지 정수를 만들어줌 , 
range1 = list(range(2,7))
print(range1)


#split() java의 그것 기본은 공백
split1 = '0 100'
split2 = '0k100'
print(split1.split())  # 0,100
print(split2.split('k')) # 0,100



# 함수
def def1():
    print('def1 print')
def1()

# 함수 매개변수

def def2(pa):
    print('def2 : '+ pa)
def2('param')

# 함수 return

def def3(pa):
    print('def3 return value : '+ pa)
    return pa
print(def3('a'))

# 참 거짓
print(1+ 1 == 2) # true
print(1+ 1 == 3) # false



##람다  함수랑 람다식##

def nolambda1(x,y):
    return x+y

print(nolambda1(10,20))
print((lambda x,y: x + y)(10,20))


# map - 자바 스트림.맵이랑 유사
map1 = list(map(lambda x : x **2, range(5)))
print(map1)

#reduce   
reduce1 = reduce(lambda x,y : x + y, [0,1,2,3,4]) #10
print(reduce1)  # 10      0+1 -> 0+1+2 ......

#filter
filter1 = list(filter(lambda x: x < 5,range(10)))
print(filter1) # [0,1,2,3,4]


#타입확인 
type1 = "d"
type2 = 0
type3 = 0.001
print(type(type1))  # str
print(type(type2))  # int
print(type(type3))  # float


#문자열 자르기
str1 = "Python"
print(str1[0:2])#Py
print(str1[:2])#Py   0부터시작시 0생략가능
print(str1[-2:]) # on   음수주면 뒷부분부터가져옴s
print(str1[::-1]) # nohtyP 역순으로 전부복사  

#문자열 소문자, 대문자
str2 = 'P@ssW0rd'
print(str2.lower()) #p@ssw0rd
print(str2.upper()) #P@SSW0RD

#특정문자 대체
str3 = 'Ruc'
print(str3.replace('c','nnnnnnnnnnnn')) #Runnnnnnnnnnnn
str4 = 'RuRuRu'
print(str4.replace('R','U'))  # UuUuUu 싹다바뀜



#매핑 (dict) - java의 map이라고 보면됨
print(type({'key':'value','key2':'value2'}));

#bool   - tf
print(type(True));


#set - 순서없는 집합
print({'1','2','3'});

