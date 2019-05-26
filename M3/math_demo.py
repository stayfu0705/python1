import math                 # 不是內建的所以要先匯入
print(math.fabs(-14.5))     # 浮點數絕對值
print(math.sqrt(25))        # 平方根
print(math.floor(3.87))     # 小於或等於的整數最大值
print(math.floor(-3.87))
print(math.ceil(3.87))      # 大於或等於的整數最小值
print(math.ceil(-3.87))
print(math.factorial(6))    # 階層值 6!
print(math.gcd(30, 72))     # 最大公約數(沒有lcd)

import random
print(random.randint(1, 100))   # 亂數產生器
