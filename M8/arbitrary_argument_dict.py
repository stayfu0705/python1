def stu(**data):
    for key,value in data.items():
        print('{}={}'.format(key,value))
def main():
    stu(name='mary',age=33,phone='0987987561',id='D123654785')
    print()
    dict1={'name':'mary','age':56,'phone':'0987987561','id':'D123654785'}
    stu(**dict1)
main()