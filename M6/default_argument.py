def sum_avg(n1,n2):
    total=0
    for i in range(n1,n2+1):
        total+=i
    avg = total/(n2-n1+1)
    return total,avg
def main():
    n1, n2 = eval(input("輸入兩個數字好嗎:"))
    total, avg = sum_avg(n1, n2)
    print('sum={0},avg={1}'.format(total, avg))
main()