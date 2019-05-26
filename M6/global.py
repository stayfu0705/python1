x=10
y=11

def main():
    x=87
    print(x)
    global y #牽一髮動全身
    y=55
    print(y)
main()
print(x)
print(y)