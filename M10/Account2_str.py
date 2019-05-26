class Account:
    def __init__(self, number, name, balance):
        self.number = number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        try:
            if amount <= 0:
                raise ValueError
            self.balance += amount
        except ValueError:
            print('金額要是正數喔')
    def withdraw(self, amount):
        try:
            if amount <= self.balance:
                self.balance -= amount
            else:
                raise ValueError
        except ValueError:
            print('餘額不足')
    def __str__(self):
        return('number = {0} name = {1} balanace = {2}'.format(self.number, self.name, self.balance))
# def main():
#     acc = Account('123456789', 'curry',0)
#     print('number = ', acc.number)
#     print('name = ', acc.name)
#     print('balance =', acc.balance)
#
#     print(acc)
#
# main()
