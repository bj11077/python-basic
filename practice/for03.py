value= input().split()
min=int(value[0])
max=int(value[1])

value2=input().split()
for x in value2:
    if x == '-999':
        print('work')
    else:
        if  min <= int(x) <= max:
            print('work')
            

# for x in range(1,value+1):
#     print(x, x*x)
