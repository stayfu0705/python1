'''def main():
    a=eval(input("輸入個數字好嗎:"))
    total =1
    for n in range (1,a+1):
        total*=n
    print(total)
main()'''

def factorial(n):#你只要管算就好了
    result=1
    for i in range (1,n+1):
        result*=i
    return result
def main (): #主函數要決定怎麼顯示
    n=eval(input("輸入個數字好嗎:"))
    print('{}!='.format(n),end='')
    for j in range (1,n+1):
        print(j,'*',end='\t')
    print('\b\b={}'.format(factorial(n)))
main()
