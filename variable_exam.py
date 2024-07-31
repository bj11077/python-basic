#지역 / 전역  어떤언어나 똑같다 근대 특별한 global이 있음
# 함수에서 반환해줄값 설정
def plus_five(x):
    a = 5
    #하지만 지역내부에서도 전역 생성가능
    global glb
    glb = 3
    return a+x


plus_five(5)

#이게뭔대
#print(a)

print(glb)



