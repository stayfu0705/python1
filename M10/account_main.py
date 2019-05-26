from M10.Checking_account import CheckingAccount
from M10.Account2_str import Account

def main():
    # acc = Account('123456789', 'curry', 0)
    # acc.deposit(8000)
    # print(acc)
    # acc.withdraw(2000)
    # print(acc)

#
    ca = CheckingAccount('8596423','annie',5000)
    ca.deposit(3000)
    print(ca.balance)
    ca.withdraw(13000)
    print(ca.balance)
    print(CheckingAccount())

main()

# def main():
#     acc = Account('123456789', 'curry',0)
#     print('number = ', acc.number)
#     print('name = ', acc.name)
#     print('balance =', acc.balance)
#     print(acc)
#
# main()

# def main():
#     acc = Account('123456789', 'curry', 0)
#     print('number = ', acc.number)
#     print('name = ', acc.name)
#     print('balance =', acc.balance)
#
#     acc.deposit(5000)
#     print('餘額:', acc.balance)
#     acc.withdraw(2000)
#     print('餘額', acc.balance)
#
#     acc1 = Account('8787', 'KD', 10000)
#     print('number = ', acc1.number)
#     print('name = ', acc1.name)
#     print('balance =', acc1.balance)
#     acc1.deposit(5000)
#     print('餘額:', acc1.balance)
#     acc1.withdraw(2000)
#     print('餘額', acc1.balance)
# main()
