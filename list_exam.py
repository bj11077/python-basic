# 리스트
primes= [3,7,11]
primes.append(5)
# 3 7 11 5
print(primes)

# 정렬가능 sort
primes.sort()
## 3 5 7 11
print(primes)

# 요소 추가 insert  (특정 위치에 추가하고싶어)
primes.insert(0,2)
#[2, 3, 5, 7, 11]
print(primes)

# 요소 삭제도됨 특정 인덱스 요소 삭제
del primes[4]
#[2, 3, 5, 7]
print(primes)

# pop으로 빼내기도 가능
print('#######')
pop_val=primes.pop()
# 7
print(pop_val)
# [2, 3, 5]
print(primes)

#리스트같은겨우에는 이렇게 수정도가능
primes[0] = 1
# [1, 3, 5]
print(primes)


# 리스트 안쪽에 리스트도 넣을수있음
orders = ['potato', ['pizza', 'Coke', 'salad'], 'hamburger']

#potato
#['pizza', 'Coke', 'salad']
#pizza
print(orders[0])
print(orders[1])
print(orders[1][0])



##### 문자열 to List
char_list=[]
str_ex='abcd efg'
for char in str_ex:
    char_list.append(char)
#['a', 'b', 'c', 'd', ' ', 'e', 'f', 'g']
print(char_list)


# 숫자형 to str
num_v=123
str_v=str(num_v)
print(type(str_v)) # str

# 리스트 원소들의 합
one_to_ten= list(range(1,11))
print(one_to_ten) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(one_to_ten)) # 55


