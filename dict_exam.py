# dictionary 사전형 자바 map같은거일듯
dic={}
dic['dictionary'] = '사전이래'
dic['python']='스타유즈맵'

#{'dictionary': '사전이래', 'python': '스타유즈맵'}
print(dic)

# 스타유즈맵
print(dic['python'])

#요소 삭제도 가능
del dic['dictionary']

#{'python': '스타유즈맵'}
print(dic)

#직접만들수도있음
family = {'mom': 'Kim', 'dad': 'Choi', 'baby': 'Choi'}
print(family)

# key값만추출
#dict_keys(['mom', 'dad', 'baby'])
print(family.keys())

# value값만추출
#dict_values(['Kim', 'Choi', 'Choi'])
print(family.values())

# items로 추출 (키/값 쌍)
#dict_items([('mom', 'Kim'), ('dad', 'Choi'), ('baby', 'Choi')])
print(family.items())


# dict 내부에 뭐가있는지 검사가능
if 'dad' in family:
    print('아빠안잔다')