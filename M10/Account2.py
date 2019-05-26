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
def main():
    acc = Account('123456789', 'curry', 0)
    print('number = ', acc.number)
    print('name = ', acc.name)
    print('balance =', acc.balance)

    acc.deposit(5000)
    print('餘額:', acc.balance)
    acc.withdraw(2000)
    print('餘額', acc.balance)

    acc1 = Account('8787', 'KD', 10000)
    print('number = ', acc1.number)
    print('name = ', acc1.name)
    print('balance =', acc1.balance)
    acc1.deposit(5000)
    print('餘額:', acc1.balance)
    acc1.withdraw(2000)
    print('餘額', acc1.balance)
main()
