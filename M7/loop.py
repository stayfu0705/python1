list1=[45,30,35,9,15,68,19,75,12,31]

for i in range(len(list1)):
    print(list1[i],end=' ')
print()
for i in list1:
    print (i,end=' ')
print()
import random
list1=[]
for i in range(6):
    list1.append(random.randint(1,100))
print(list1)