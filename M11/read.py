with open('long.txt', 'r') as f:
    line = f.readline()
    while line != '':
        print(line, end='')
        line = f.readline()
print('------------------------')
with open('long.txt', 'r') as f:
    line = f.readline()
    while line != '':
        print(repr(line))
        line = f.readline()
print('------------------------')
with open('long.txt', 'r') as f:
    data = f.read(10)
    print(data)
    print('------------------------')
    data = f.read(10)
    print(data)
    print('------------------------')
    data = f.read(10)
    print(data)
print('------------------------')
with open('long.txt', 'r') as f:
    data = f.readlines()
    print(data)
print('------------------------')
with open('long.txt', 'r') as f:
    data = f.readlines(8)
    print(data)
with open('long.txt') as f:
    print('------------------------')
    print(f.read())
    print('------------------------')
    f.seek(19)
    print(f.read())
    print('------------------------')
    f.seek(os.SEEK_END)
    print(f.read())