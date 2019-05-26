def outer():
    def inner1():
        def inner2():
            print(87)
        inner2()
    def inner3():
        def inner4():
            print(99)
        inner4()
    inner3()
    inner1()

outer()
#inner1() 如果打在這邊在肚子外面的不會引用到
