def msg(name,age):
    print("{} is a {} years old.".format(name,age))
def main():
    msg("mary","24")
    msg(name='mary',age=34)
    #msg(age=30, 'andy')
    msg('andy',age=25)
main()