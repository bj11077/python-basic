# 파이썬에서의 값변경

a = 10
b = 20
a , b = b , a
#20 10
print(a,b)


# 튜플 사용처
# 자바 (ss...) 같은거인듯
#1 2
#(3, 4, 5, 6, 7, 8, 9)
def lot_print(x,y,*rest):
    print(x,y)
    print(rest)

lot_print(1,2,3,4,5,6,7,8,9)



# 튜플선언
tup_ex01 = ('a','b','c')

#빈거도 선언가능
tup_empty = ()

#원소 하나만 가진 튜플은 ,로 생성가능
tup_only_one= 5,
#(5,)
print(tup_only_one)

# 튜플은 리스트와 달리 원소값을 직접 바꿀수없고 오려붙여야됨
p = (1,2,3)
q = p[:1] + (5,) + p[2:]
print(q)