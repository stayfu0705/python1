x=10
print(x)
y=10
print(y)
print(id(x))
print(id(y))
z=x
print(z)
print(id(z))

x=20
print(x)
print(id(x))

a,b=30,35
print(a)
print(b)
print(id(a))
print(id(b))

a=b=c=5
print(id(a))
print(id(b))
print(id(c))

x=x+1
print(x)

p=100
print(p)
print(id(p))

p=p+1
print(p)
print(id(p))


