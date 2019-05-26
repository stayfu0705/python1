dict1={'name':"curry",'age':30,"mobile":'0911222365'}
print(dict1)
print(type(dict1))
dict1={'name': "curry", 'age': 30, "phone": '0911222365'}

for key in dict1:
    print('{}:{}'.format(key,dict1[key]))


print(dict1.values())
print(list(dict1.values()))
print(list(dict1.keys()))

print(dict1.values())
print(list(dict1.values()))
print(list(dict1.values()))

print(dict1.items())
print(list(dict1.items()))
print(list(dict1.items()))

for key in dict1.keys():
    print(key)          #印出KEY值
for val in dict1.values():
    print(val)          #印出val
for data in dict1.items():
    print(data)
for key, value in dict1.items():
    print("{}:{}".format(key, value))