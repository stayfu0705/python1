'''n=0
total = 0
while n <= 100:
    total += n
    n += 1
print(total)

n=10
total = 0
while n >= 0:
    total += n
    n -= 1
print(total)

total =0
for n in range(10,0,-1):
    total +=n
print(total)'''
print('{name} is {age} years old'.format(age='30',name='andy'))