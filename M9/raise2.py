try:
    n1,n2=eval(input("plz input two numbers to divide:"))
    num= n1/n2
    print("{}/{}={}".format(n1,n2,num))
except SyntaxError:
    print('是不會打逗號喔')
except ZeroDivisionError:
    print('除數不能是零拉')
except:
    print('我也不知道 反正你是錯了')
else:
    print("阿不就好棒棒")
finally:
    print('ㄅㄅ')