set1={11,22,33,44,55}
set2={99,88,77,66,55}
set={}

print(set1.union(set2)) #連集
print(set1.intersection(set2)) #交集
print(set1.difference(set2)) #差集
print(set1.symmetric_difference(set2)) #對稱差集
print(set1.union(set2).difference(set1.intersection(set2)))
print("---------------------------------------------")
print(set1 & set2) #交集
print(set1 | set2) #連集
print(set1-set2) #差集
print(set1^set2) #對稱差集
print("---------------------------------------------")
set1={1,2,5,98,3,6,4,23}
set2={1,2}
print(set1.issubset(set2)) 
print(set2.issubset(set1))
