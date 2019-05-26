tuple1=(31,85,3,8,54,21,30,54,35,89)
for data in tuple1:
    print(data)
tuple1=((31,85),(3,8),(21,30),(54,35))
for data in tuple1:
    print(data) #會印出三個tuple
print('----------------------------------------------')

for data in tuple1:
    for data1 in data:
        print(data1,end=" ")
    print()
# 迴圈印出所有tuple的值