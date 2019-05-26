x=[i for i in range(1,11)] # list 可變
print(x)
x=[i*10 for i in range(1,11)]
print(type(x))
print(x)
x={i for i in range(1,11)}
print(x)
x={i:i*10 for i in range(1,11)} # dict可變
print(type(x))
print(x)

x=(i for i in range(1,11)) # tuple不可變
print(x)

#  印出偶數
for y in x:
    print (y)
x=[i for i in range(2,31,2)]
print(x)

x=[i for i in range(1,31) if i%2==0]
print(x)

x=[i for i in range(1,31) if i%2]
print(x)
#  印出奇數
x=[i for i in range(1,31) if i%2]
print(x)

#小於一百的質數 還沒寫完
x=[i for i in range(1,101) if i%i==0]
print(x)
