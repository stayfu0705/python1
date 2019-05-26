# 寫一函數power(x, n)用來計算x的n次方。
# 說明：power (5,3)即計算5的3次方
# def pow(x,n):
#     c=1
#     for i in range (1,n+1):
#         c*=x
#     return c
# def main():
#     x,y=5,3
#     z=pow(5,3)
#     print('pow({0},{1})={2}'.format(x,y,z))
# main()
############################################################
# 2.	函數的練習-sigma
# def pow(x,n):
#     c=1
#     for i in range (1,n+1):
#         c*=x
#     return c
# def factorial(n):
#     result=1
#     for i in range (1,n+1):
#         result*=i
#     return result
# def my_func(x,n):
#     f = 0
#     for i in range(1, n + 1):
#         f += pow(x, i) / factorial(i)
#     return f
#
# def main():
#
#     print("{}".format(my_func(3,3)))
#
# main()
############################################################
# 3.寫一函數is_prime(n)用來判斷n是否為質數。
# def is_prime(a):
#     for i in range(2,a):
#         if a%i==0:
#             print(a, '不是質數')
#             break
#     else:
#         print(a,'是質數')
#     return a
# def main():
#     n = eval(input('輸入一個數字:'))
#     print(" ".format(is_prime(n)))
# main()
############################################################
# 寫一函數get_prime (n)用來找出第n個質數。
# def is_prime(a):
#     count=0
#     for i in range(1,a+1):
#         if a%i==0:
#            count+=1
#     if count==2:
#         return True
#     else:
#         return False
# def get_prime(n):
#     i = 0
#     count = 0
#     while i >= 0:
#         i+=1
#         if is_prime(i) is True:
#            count+=1
#         if count==n:
#             print(i)
#             break
# def main():
#     b = eval(input('你想找第幾個質數阿:'))
#     print(" ".format(get_prime(b)))
# main()
############################################################
# 寫一函數is_mersenne_prime(n)用來判斷n是否為Mersenne質數。
# 撰寫一程式找出前5個Mersenne質數。
# def is_prime(a):
#     count=0
#     for i in range(1,a+1):
#         if a%i==0:
#            count+=1
#     if count==2:
#         return True
#     else:
#         return False
# def get_mersenneprime(b):
#     i = 0
#     count = 0
#     while i >= 0 and count != b:
#         i+=1
#         if is_prime(2**i-1):
#            count += 1
#            print(2 ** i - 1)
#         # if count == b:
#         #     break
# def main():
#     b = eval(input('要印幾個梅森質數:'))
#     print(" ".format(get_mersenneprime(b)))
# main()
############################################################
# 6.	遞迴函數的練習-factorial_recursive
# 寫一遞迴函數factorial (n)用來計算1*2*3*…*n的值。
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n*factorial(n-1)
# def main():
#     n=eval(input('輸入一個數字:'))
#     print('{0}!={1}'.format(n, factorial(n)))
# main()
############################################################
# 7.寫一遞迴函數sum (n)用來計算2+4+6…+2n的值。
# def sum(n):
#     if n == 0:
#         return 0
#     else:
#         return 2*n+sum(n-1)
# def main():
#     a=eval(input('輸入一個數字:'))
#     print('sum={1}'.format(a, sum(a)))
# main()
############################################################
# 輸入一整數，寫兩個函數分別為to_binary(n)和to_hexadecimal(n)
# 用來將n轉換成二進制和十六進制的值。(勿使用任何現成的函數)

def to_binary(a):
    total = 0
    count=0
    while a > 0:
        if a%2 == 0 :
             total = total/10
        else:
             total = (total+1)/10
        a = a//2
        count+=1
    return round(total*10**(count))
def main():
    n = eval(input('輸入一個數字:'))
    print('{0} 的二進位是 {1}'.format(n, to_binary(n)))
main()

