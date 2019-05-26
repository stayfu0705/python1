def func(n):
    print('level',n)
    print("LEVEL", n)
    if n<4:
        func(n+1)
    print("LEVEL",n)
def main():
    func(1)

main()