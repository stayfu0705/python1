'''
num=eval(input('input ur month:'))
if  num in (12,1,2):
    print("冬天!")
elif  num in (3,4,5):
    print("春天!")
elif  num in (6,7,8):
    print("夏天!")
elif  num in (9,10,11):
    print("秋天!")
else:
   print("輸入錯誤")
'''

'''a=eval(input('輸入你的工時:'))
if a<60:
    print(a*120,'元')
elif a>=61 and a<=80:
    print(60*120+(a-60)*120*1.25,'元')
elif a>=81:
    print(60*120+20*120*1.25+(a-80)*120*1.5,'元')
else:
    print('滾拉廢物')'''

# a=eval(input('輸入你的用電種類 1=家用,2=工業用:'))
# b=eval(input('輸入你的用電量:'))
# if a==1 or a==2:
#     if a==1 and b<=240:
#         print(b*0.15)
#     elif a==1 and 240<b<=540:
#         print(240*0.15+(b-240)*0.25)
#     elif a == 1 and b>540:
#         print(240 * 0.15+300*0.25+(b - 540) * 0.45)
#     elif a==2 and b>0:
#         print(b*0.45)
# else:
#     print("掰掰")

'''a=eval(input('輸入一個西元年分:'))
if  a%4000==0:
    print('非潤')
elif a%400==0:
    print('潤')
elif a%100==0:
    print('非潤')
elif a%4==0:
    print('潤')
else:
 print('選個偶數再來吧')'''

'''a=eval(input('購買金額:'))
b=eval(input('實付金額:'))
if a<b:
    print((b-a)//1000,'張一千',(b-a)//500,"張五百"
          ,(b-a)%500//100,"張一百"
          ,(b-a)%100//50,"個50元",(b-a)%50//10,"個10元"
          ,(b - a) % 10 // 5, "個五元"
          ,(b-a)%5,"個1元")
elif a==b:
    print("免找")
else:
    print("付錢拉廢物")'''
'''import math
print('ax^2+bx+c')
a=eval(input('係數a:'))
b=eval(input('係數b:'))
c=eval(input('係數c:'))
d=b**2-4*a*c
if d>0:
    print("有相異實根")
    print((-b + math.sqrt(d)) / 2 * a)
    print((-b - math.sqrt(d)) / 2 * a)
elif d==0:
    print((-b + math.sqrt(d)) / 2 * a,"重根")
else:
    print("虛根")'''
