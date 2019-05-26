a = 123
b = 12345.678
c = "Python"

print('/' + format(a, '5d') + '/')      # 5表示總共要印五個字元，不夠的話左邊會有空格
print(format(a, '05d'))     # 空格改補0
print(format(a, '+5d'))     # 顯示正負號
print('/' + format(a, '<5d') + '/')     # 要用<才是向左靠，不是-
print(format(a, '#x'))      # 以16進位呈現，x可以大寫
print(format(a, '#o'))      # 以8進位呈現但o不能大寫
print(format(a, '#b'))      # 以2進位呈現(另一個格式化沒法做到)
# print(format(a, '#B'))      # 但b不能用大寫

print(format(b, 'f'))
print(format(b, '.2f'))
print(format(b, '10f'))
print('/' + format(b, '10.2f') + '/')
print('/' + format(b, '<10.2f') + '/')
print('/' + format(b, '10.2E') + '/')

print('/' + format(c, '10s') + '/')     # 字串format中預設是向左靠，所以空白在右邊
print('/' + format(c, '>10s') + '/')    # >表示向右靠
print('/' + format(c, '^10s') + '/')    # ^表示置中

print('/' + format(c, '*>10s') + '/')   # 填滿字元
print('/' + format(c, '*<10s') + '/')
print('/' + format(c, '*^10s') + '/')

print('/' + format(b, '10,.2f') + '/')  # 千位符號