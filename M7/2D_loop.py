# list1=[[1,2,3],[7,8,9]]
# for i in range(len(list1)):
#     for j in range(len(list1[0])):
#         print(list1[i][j],end=' ')
# print()
list2=[[1,2],[35,70],[18,39]]
a=0
for i in range(len(list2)):
    for j in range(len(list2[i])):
        a+=list2[i][j]

        print(a,end=' ')
print()
#
#
# for i in range(len(list1)):
#     print(list1[i], end=' ')
#
# import random
# list=[]
# row,col = eval(input("input row and col:"))
# for i in range(row):
#     list.append([])
#     for j in range(col):
#         list[i].append(random.randint(1,100))
# print(list)