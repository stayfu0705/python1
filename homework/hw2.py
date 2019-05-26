  # 第一題
# n=1
# total=0
# while n<50:
#     total+=-(2*n+1)
#     n+=2
# print(total)

# 輸入一正整數，求其所有的因數。
# a=eval(input('輸入一個數字:'))
# for n in range(1,a+1):
#      if a%n==0:
#          print(n,end=' ')

# a=eval(input('輸入一個數字:'))
# count=0
# for n in range(1,a+1):
#     if a % n == 0:
#         count+=1
# if  count==2:
#     print(a,'是質數')
# else:
#     print(a,'非質數')

#一個數字若等於其所有因數的總和，則此數為perfect number。
#找出100以內所有的完美數。
# a=eval(input('輸入一個數字:'))
# for i in range(2,a+1):
#     fs=1                            #因為因數一定有1 所以先+在裡面當作預設值是1
#     for j in range(2,i):
#         if i%j==0:
#             fs+=j
#     if fs==i:
#         print(fs)

# Amstrong數是指一個三位數的整數，其各位數之立方和等於該數本身。
# 找出所有的Amstrong數。
# for a in range(100,1000):
#     if  (a//100)**3+((a%100)//10)**3+(a%10)**3==a:
#         print('阿姆斯壯 壯起來',a)



# a=int(input('輸入一個數字:'))
# for i in range(2,a):
#     for j in range(2, i):
#         if a%i==0:
# if j<=i:
#     print(j)


#輸入一正整數，找出所有小於或等於的質數。
# import math
# a=eval(input('輸入一個數字:'))
# for i in range(2,a+1): #先圈出i的範圍(2~a+1)
#     j = 2
#     prime = True
#     while j <= math.sqrt(i): #找  根號i=j
#         if i%j == 0:         #如果i可以被j整除
#             prime = False    #那就失敗了 不能取 換下一位
#             break            #所以我這邊要一個break
#         j=j+1                #做完j換j+1上去繼續
#     if prime:                #那如果上面那個if條件不行
#        print(i,'是質數')     #跳出迴圈表示說我這是一個質數 就印出來

#質數第二種寫法
# a=eval(input('輸入一個數字:'))
# for i in range(2,a+1):
#     count=0
#     for j in range(2,i-1):
#         if i%j==0:
#             count +=1
#     if count == 0:
#         print(i,end=' ')
#若有一條繩子長3000公尺
# 每天剪去一半的長度，需多少天繩子的長度會短於5公尺。
# count=0
# l=3000
# while l>=5:
#     count=count+1
#     l=l/2
# print(count)

# for m in range(0,i):
#     for i in range(0, ):
#         if m%7==2and m%5==3 and m%3==1:
#             m=m
#             print(m)

# 老王養了一群兔子，若三隻三隻一數，剩餘一隻；若五隻五隻一數，剩餘三隻；
# 若七隻七隻一數，剩餘二隻。試問兔子最少有幾隻。
# a=1
# while a>=1:
#     if a % 7 != 2 or a % 5 != 3 or a % 3 != 1: #可以直接放到while條件裡面
#         a+=1
#     else:
#         break
# print(a)
#解法2
# a = 0
# while a >= 0:
#      a += 1
#      if a % 3 == 1 and a % 5 == 3 and a % 7 == 2:
#          break
# print(a)

# 出現”請輸入密碼”的提示，使用者有最多三次輸入的機會。
# 若輸入正確，則印出”密碼輸入正確，歡迎使用本系統！”。
# 若輸入不正確，再次出現”請輸入密碼”的提示。
# 若三次輸入不正確，則印出”密碼輸入超過三次！”，並結束程式的執行。

# count=1
# a=eval(input('輸入一個4位數字:'))
# while a != 1234:
#     a = eval(input('輸入一個4位數字:'))
#     count += 1
#     #print(count)
#     if count == 3 and a != 1234:
#         print("滾拉")
#         break
#     if count < 3:
#         a == 1234
# else:
#     print("歡迎使用")

########################錯誤示範###################
# count=0
# while eval(input('輸入一個4位數字:')) != 1234:
#     count += 1
#     print(count)
#     if count == 2:  #A條件
#         print("滾拉")
#         break
#     if eval(input('輸入1個4位數字:')) == 1234:  #B條件
#         print("歡迎使用")
#         break #錯的 會先執行A條件再跑B條件
###################################################

# 9.	迴圈敘述的練習-stars
#    畫出下列三種排列的星星圖形。
#
#  (1)	*          (2) * * * * *    (3)  	 *
#       * *              * * * *            *  *
#       * * *              * * *           *  *  *
#       * * * *              * *          *  *  *  *
#       * * * * *              *         *  *  *  *  *
# (1)
# total=0
# for n in range(1,6):
#     total+=1
#     print("{}".format('* '*n),end="\n")
#(2)
# n=6
# while n>=1:
#     n-=1
#     print("{}".format('* ' * n), end="\n")
#(3)
# total=0
# for n in range(1,6):
#     total+=1
#     print(" "+format('* '*n,'^10s')+" ",end="\n") #P.54 有format格式

# 10.	迴圈敘述的練習-nine_nine
#    印出下列九九乘法表

# print("   |   ",end="")
# for n in range(1,10):
#     print("\b{}     ".format(n),end="  ")
# print()
# print("-------------------------------------------------------------------")
#
# for i in range(9, 0, -1):
#     print("{}  |".format(i), end=" ")
#     for j in range(1, 10, 1):
#         if j<=i:
#             print(" {}".format(i*j), end="    ")
#     print()
# 錢精打以10%單利投資100000元，郝細算則以5%複利投資100000元。
# 計算多少年後郝細算的投資可以超過錢精打，並將此時兩人錢數印出。(27年後)
# 提示：單利公式：P(1+r*n)    複利公式：P(1+r)n
# #
# n=0
# while n>=0:
#     n=n+1
#     if(1+0.1*n)<=(1+0.05)**n:
#         break
# print(n)



# 12.	迴圈敘述的練習-loan
# 錢不精以100000元分別向銀行、當鋪和地下錢莊借貸。
# 若銀行的年利率為20%，
# 當鋪月利率為10%
# 地下錢莊日利率為1%。以月為單位，計算一個月後至一年後每個月該歸還多少錢。(單利)

# total=0
# for n in range (1,13):
#     total=100000*(1+0.2/12*n)
#     n+=1
#     print("{0}月後要還銀行{1}元".format(n-1,round(total)))
#
# total=0
# for n in range (1,13):
#     total=100000*(1+0.1*n)
#     n+=1
#     print("{0}月後要還當鋪{1}元".format(n-1,round(total)))
#
# total=0
# for n in range (1,13):
#     total=100000*(1+0.3*n)
#     n+=1
#     print("{0}月後要還當鋪{1}元".format(n-1,round(total)))
