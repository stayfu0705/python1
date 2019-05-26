list1=[]
list1.append(30)
list1.append(11)
list1.append(35)
list1.append(4)
print(list1)
list1.insert(0,87) #指名87要在0上插隊
print(list1)
print(list1.pop()) # 挑出最後一個 把他殺了
print(list1) #顯示最後一個被殺掉的結果
print(list1.pop(0))  # 挑出第一個 把他殺了
print(list1)
list1.remove(11) # 直接殺了 如果有重複的11 就先殺第一個
print(list1)
print(list1.index(30)) # 取得30的位置
print(list1.count(30)) # 取得30出現的次數
list1.remove(30)
print(list1)
list3=[25,14,57,26,15,65,98]
list3.reverse() # 反轉
list3.sort() #小排到大
print(list3)
list3=[25,14,57,26,15,65,98]
list3.sort() #小排到大
list3.reverse() # 反轉
print(list3)


str1='curry andy james'
list1=str1.split(',')
print(list1)
str1='pytjon,    java,c'
list1=str1.split(',') #切字串
for val in list1:
    print(val)
