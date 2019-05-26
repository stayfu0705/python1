list1=[[[1,2],
        [3,4]],

       [[5,6],
        [7,8]],

       [[10,11],
        [62,88]]]
print(list1)

print(list1[0][0][0],end=' ')
print(list1[0][0][1],end=' ')
print(list1[0][1][0],end=' ')
print(list1[0][1][1],end=' ')

print(list1[1][0][0],end=' ')
print(list1[1][0][1],end=' ')
print(list1[1][1][0],end=' ')
print(list1[1][1][1],end=' ')

print(list1[2][0][0],end=' ')
print(list1[2][0][1],end=' ')
print(list1[2][1][0],end=' ')
print(list1[2][1][1],end=' ')
print()
list1 = [[[1, 2],
          [3, 4]],

         [[5, 6],
          [7, 8]],

         [[10, 11],
          [62, 88]]]

for i in range(len(list1)):
    for j in range(len(list1[i])):
        for k in range(len(list1[i][j])):
            print(list1[i][j][k],end=' ')
print()