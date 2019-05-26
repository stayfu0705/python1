x=10
y=11
def outer():
    x=87
    def inner():
        x=30
        print(x)
        print(y)
    inner()
    print(x)
    print(y)
outer()
print(x)
print(y)