dict1={'name': "curry", 'age': 30, "phone": '0911222365'}
print(len(dict1))
print('name' in dict1)
print('Tom' in dict1)

dict2={'age': 22, 'mobile': '0988884878', 'name': 'bill'}
print(dict1 == dict2)
print(dict2)

# tuple1=(31,85,3,8,54,21,30,54,35,89)
# print(tuple1)
# tuple1 += (33, 2)
# tuple1 += (48,)
#
# del dict1['age']
# print(dict1)
#
# print(dict1.pop('phone'))
# print(dict1)
# dict1.clear()
# print(dict1)
#
dict2 = dict1.copy()
print(dict1)
print(dict2)

dict1={'name':'andy', 'mobile': '09000224878', 'age': '33'}
dict2={'age': 22, 'mobile': '0988884878', 'name': 'bill'}
dict1.update(dict2) #dict1是被改的
print(dict1)  #會印出被改過後的東西
print(dict2) # 沒變
