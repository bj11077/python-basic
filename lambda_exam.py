
# 해당 함수를 람다로
def plus_each(x,y):
    return x + y

print(plus_each(10,20))


lambda_result = (lambda x,y: x + y)(10,20)

print(lambda_result)