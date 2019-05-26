import M6.mymath  # 用之前先import要加package name.檔案名稱(別種寫法見p.105)
a=M6.mymath.mypow(3,4)  # 不能直接用 要加上前導字元
print(a)
b=M6.mymath.myabs(-9)
print(b)
c=M6.mymath.mysum(8,9)
print(c)

import M6.mymath as m #用別名
a=m.mypow(3,4)
print(a)
b=m.myabs(-9)
print(b)
c=m.mysum(8,9)
print(c)

from M6.mymath import mypow
print(mypow(2,3))

from M6.mymath import *
print(mypow(2,3))