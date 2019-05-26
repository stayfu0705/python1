from M10.Account2_str import Account
class CheckingAccount(Account):
    def __init__(self, number, name, balance=0, credit_limit=10000):
        super(CheckingAccount, self).__init__(number,name,balance)
        self.credit_limit = credit_limit

    def withdraw(self, amount):
        try:
            if amount > self.balance+self.credit_limit:
                raise ValueError
            else:
                self.balance -= amount
        except ValueError:
            print('太超過囉')
    def __str__(self):
        return super(CheckingAccount, self).__str__() \
        +',credit_limit={}'.format(self.credit_limit)
def main():
    acc=CheckingAccount('112336','hank')
    print(acc)
    amount=int(input('輸入存款金額:'))
    acc.deposit(amount)
    print(acc.balance)
    amount = int(input('輸入提款金額:'))
    acc.withdraw(amount)
    print(acc.balance)
main()

