
s = input("Input a String:")
print(s)

first = input("input your firstname:")
last = input("input your lastname:")
print(first, last)


salary = input("input your salary: ")
print('annualSalary={}'.format(salary * 12))       # 沒包int會變成複製字串12次

salary = int(input("input your salary: "))
print('annualSalary={}'.format(int(salary) * 12))


salary = float(input("input your salary: "))             # 如果輸入的值是浮點數
print('annualSalary={}'.format(int(salary) * 12))

salary = eval(input("input your salary: "))             # int跟float都可以用
print('annualSalary={}'.format(int(salary) * 12))

x, y = eval(input("input your salary: "))               # 若一次輸入兩個值以上就不能用int改用eval，
print('total = {}'.format(x * y))
