x=10
def outer():
    x=20
    def inner():
        y=30

        def inner1():
            nonlocal x #只有在定義裡面生效
            print(x)
            x=40
        inner1()
        print(x)
        print(y)
    inner()
    print(x)
outer()
print(x)