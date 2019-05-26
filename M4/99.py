for i in range(1, 10):
    for j in range(1, 10):
        print("{0}*{1}={2}".format(i, j, i*j), end="\t")
    print()
print("=====================================")
for j in range(1, 10):
    for i in range(1, 10):
        print("{0}*{1}={2}".format(i, j, i*j), end="\t")
    print() #先跑j再跑i
print("=====================================")
for i in range(9, 0, -1):
    for j in range(9, 0, -1):
        if j<=i:
            print("{0}*{1}={2}".format(i, j, i*j), end="\t")
    print()
print("=====================================")
for i in range(1, 10):
    for j in range(1, 10):
        print(i*j, end="\t")
    print()