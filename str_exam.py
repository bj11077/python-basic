# 문자열의 내용물 찾기

str = 'banana'

# 0번째 글자?  b
print(str[0])

# 2번부터 3번까지의 글자 na
print(str[2:4])

# 3번 앞까지의 글자 ban
print(str[:3])

# 3번부터 끝까지  ana
print(str[3:])


# 특정문자위치찾기 없으면 -1
str_two= 'hello Python!'

wrong_idx =str_two.find('p')
correct_idx=str_two.find('P')
print('############')
print(wrong_idx)
print(correct_idx)
# Python!
print(str_two[correct_idx:])


# 공백삭제기능 
#rstrip : 문자열에 오른쪽 공백이나 인자가된 문자열의 모든 조합을 제거
#lstrip : 문자열에 왼쪽 공백이나 인자가된 문자열의 모든 조합을 제거
# stripo : 양옆의 공백모두제거
rs_exam='hello '
print(len(rs_exam))  #6
print(len(rs_exam.rstrip())) #5


#split  기본적으론 공백으로 나눔
str_three= 'hello Python!'
str_list=str_three.split()
print(str_list) # [hello, python!]

