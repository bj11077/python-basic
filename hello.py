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


# map 자바랑 유사
map1 = list(map(lambda x : x **2, range(5)))
print(map1)

#reduce   
reduce1 = reduce(lambda x,y : x + y, [0,1,2,3,4]) #10
print(reduce1)  # 10      0+1 -> 0+1+2 ......

#filter
filter1 = list(filter(lambda x: x < 5,range(10)))
print(filter1) # [0,1,2,3,4]


#4. 데이터타입부터 봐야됨
