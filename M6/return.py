def total(x,y):
    z=x+y
    return z
def main():
    a,b=eval(input("輸入兩個數字好嗎:"))
    c=total(a,b)
    print('{0}+{1}={2}'.format(a,b,c))
main()
