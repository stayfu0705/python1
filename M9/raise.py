try:
    score=int(input('input a score:'))
    if score<0 or score>100:
        raise ValueError
    else:
        print(score)
except ValueError:
    print('plz input 1~100')
