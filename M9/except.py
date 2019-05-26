try:
    num = int(input('plz input a number:'))
    print('{} is a {} number'.format(num,'odd' if num%2 else'even'))
except ValueError as e:
    print(e)
