tuple1 = ('python','java','c','c#')
print(tuple1)
print(tuple1[0])
print('c' in tuple1)
print(tuple1*0)
# tuple1.append("andy") #tuple沒提供append
print(tuple1)

list1=[]
list1.append(34)
list1.append(65)
list1.append(18)
list1.append(30)
tuple1=tuple(list1)
print(tuple1)

str1='curry'
tuple1=tuple(str1)
print(tuple1)

tuple1=(31,85,3,8,54,21,30,54,35,89)
print(tuple1)
print('-----------------------------')
tuple1 + (31,85,3,8,54,21,30,54,35,89)  # 要在數組裡面加數字要這樣+
tuple1 += (48,)  # 只要加一個元素的話最後面要加逗號
print(tuple1)
list1=list(tuple1)
print(list1)