print('{0} is {1} years old!'.format('Tom', 30))        # 可給數字當作順序，從0開始
print('{1} is {0} years old!'.format('Tom', 30))        # 反過來當然可
print('{0} is {0} years old!'.format('Tom', 30))
print('{} is {} years old!'.format('Tom', 30))          # 也可以不給數字，就照預設順序排

print('{name} is {age} years old!'.format(name='Tom', age=30))      # 也可以用關鍵字表示
print('{name} is {age} years old!'.format(age=30, name='Tom'))      # 參數順序反了也沒問題

print('{0} is {age} years old!'.format('Tom', age=30))              # 還能混和雙打，但一定要position在keyword前
# print('{name} is {1} years old!'.format(name='Tom', 30))            # 倒過來compile就不會過

print('{0}, {1}# {2}'.format(123, 12345.678, "Python1"))
print('{}, {}# {}'.format(123, 12345.678, "Python2"))
print('{0}, {1:.2f}# {2}'.format(123, 12345.678, "Python3"))
print('{}, {:.2f}# {}'.format(123, 12345.678, "Python4"))        # 冒號不能省略

sec = 345
print('{}秒 = {}分{}秒'.format(sec, sec//60, sec%60))