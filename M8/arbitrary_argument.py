def greet(*names):
    for name in names:
        print('GG3B0',name)
def main():
    greet('mary','marty','jean','annie','curry')
    print()
    names=('mary','marty','jean','annie','curry')
    greet(names)   # 這樣會變成後面跟一群人沒有隔開
    greet(*names)   # 加星星之後就可以了
    print()
    names = {'mary', 'marty', 'jean', 'annie', 'curry'}
    greet(*names)

    names='andy'
    greet(names)    # 跟上面一樣
    greet(*names)  # 變成單字拆開

main()