class Account:
    pass
def deposit(acc,amount):
    try:
        if amount<=0:
            raise  ValueError
        acc.balance+=amount
    except ValueError:
        print('金額要是正數喔')
def withdraw(acc,amount):
    try:
        if amount<=acc.balance:
            acc.balance-=amount
        else:
            raise  ValueError
    except ValueError:
        print('餘額不足')
def main():
    acc=Account()
    acc.number='123456789'
    acc.name='curry'
    acc.balance=0

    print(acc.number)
    print(acc.name)
    amount=int(input('請輸入存款金額:'))
    deposit(acc,amount)
    print('餘額:',acc.balance)
    amount=int(input('請輸入提款金額:'))
    withdraw(acc,amount)
    print('餘額',acc.balance)
main()
