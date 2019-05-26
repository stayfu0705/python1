def greet(*names):
     for name in names:
         print('GG3B0',name)

def stu(**data):
    for key,value in data.items():
        print("{} is {}".format(key, value))

def main():
    greet('mary', 'marty', 'jean', 'annie', 'curry')
    print()
    stu(name='mary',age=56,mobile='091212121212',id='A44444444')
main()