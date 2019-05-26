#########################################################################
# 1.一維串列的練習-max_min
# 事先將10個數字置於串列中，分別找出10個數字中最大的值和最小的值。
# list1 = [30, 25, 68, 2, 48, 24, 23, 9, 33, 15]
# max = list1[0]
# for i in range(1,10):
#     if int(list1[i-1]) >= max:
#         max=list1[i-1]
# print (max)
#
# min = list1[0]
# for i in range(1,10):
#     if int(list1[i-1]) <= min:
#         min=list1[i-1]
# print (min)
#########################################################################
# list1=[[1, 2, 27,30], [9, 8, 7,15], [8, 5, 2,25]]
# def AVG():
#     sum = 0
#     for i in range(len(list1)):
#         for j in range(len(list1[i])):
#             sum+=list1[i][j]
#     return sum/(len(list1)*len(list1[i]))
# def max():
#     max = list1[0][0]
#     for i in range(len(list1)):
#         for j in range(len(list1[i])):
#             if int(list1[i][j]) >= max:
#                 max=list1[i][j]
#     return max
# def min():
#     min = list1[0][0]
#     for i in range(len(list1)):
#         for j in range(len(list1[i])):
#             if int(list1[i][j]) <= min:
#                 min=list1[i][j]
#     return min
# def avg():
#     list2=[]
#     for i in range(len(list1)):
#         sum=0
#         for j in range(len(list1[i])):
#             sum+=list1[i][j]
#         list2.append(round(sum/len(list1)))
#     return list2
# def main():
#     # print('平均值:', AVG())
#     # print('最大值:', max())
#     # print('最小值:', min())
#     print('每組平均:', avg())
# main()
#########################################################################
# list1=[[33,77,43],[32,33,55],[56,68,43],[45,45,67],[33,23,65]]
# list2=[12,16,10,14,15]
# list3=['產品A','產品B','產品C','產品D','產品E']
# list4=['Jean','Tom','Tina']
# a.	每一個銷售員的銷售總金額
# def a():
#     lista=[]
#     for i in range(len(list1[0])):# 0-2
#         sum=0
#         for j in range(len(list1)):  #0-4
#             sum += list1[j][i]*list2[j]
#         lista.append('{} 總金額是 {}'.format(list4[i], sum))
#     return lista

# b.	有最好業績（銷售總金額最多者）的銷售員
# def b():
#     listb=[]
#     max = 0
#     for i in range(len(list1[0])):# 0-2
#         sum=0
#         for j in range(len(list1)):  #0-4
#             sum += list1[j][i]*list2[j]
#         if sum>=max:
#             max = sum
#     listb.append('{} 總金額是 {}'.format(list4[i], max))
#     return listb
#
# c.	每一項產品的銷售總金額
# def c():
#     sum=0
#     count=0
#     listc=[]
#     for i in range(len(list1)):
#         for j in range(len(list1[i])):
#             count+=1
#             sum+=list1[i][j]
#             if count%3==0:
#                 listc.append('{}總金額是{}'.format(list3[i],sum*list2[i]))
#                 sum=0
#                 count=0
#     return listc

# d.	銷售總金額最多的產品
# def d():
#     listd=[]
#     for i in range(len(list1)):
#         sum = 0
#         for j in range(len(list1[i])):
#             sum+=list1[i][j]*list2[i]
#         listd.append(sum)
#     print('{}---{}'.format(list3[listd.index(max(listd))],max(listd)))


# def main():
    # print(a())
    # print(b())
    # print(c())
    # d()  # 這裡可以不用寫print,直接寫函數名稱就好
# main()
#########################################################################
listrain=[[[21.8,198.0,147.0],   # 總和=2147.3
           [98.1,634.7,384.4],
           [222.1,84.0,198.9],
           [25.5,46.0,86.8]],

           [[20.0,90.0,182.0],  # 總和=2519.2
            [87.6,302.8,248.3],
            [316.8,728.2,309.9],
            [135.3,22.6,75.7]],

            [[256.0,78.9,285.7],  # 總和=2431.7
            [184.4,186.7,429.8],
            [174.6,141.4,428.5],
            [137.6,111.6,16.5]],

           [[21.8,123.7,182.7],  # 總和=2339.7
            [121.5,135.5,649.7],
            [206.6,166.2,175.6],
            [368.6,120.9,66.9]],

           [[255.8,163.6,37.3],  # 總和=1621.0
            [59.6,42.0,119.8],
            [190.3,186.8,321.9],
            [125.1,64.4,54.4]]]
listyear = [2014, 2015, 2016, 2017, 2018]
listseason = ['春','夏','秋','冬']
# def allavg():
#     sum=0
#     for i in range(len(listrain)):
#         for j in range(len(listrain[i])):
#             for k in range(len(listrain[i][j])):
#                 sum+=listrain[i][j][k]
#     return sum
#
# def yearavg():
#     count = 0
#     for i in range(len(listrain)):
#         sum = 0
#         for j in range(len(listrain[i])):
#             for k in range(len(listrain[i][j])):
#                 count+=1
#                 sum += listrain[i][j][k]
#                 if count%3==0:
#                     break
#         print('{}的{}'.format(listyear[i],sum/12))

def seasonavg(a):
    for i in range(len(listrain[a-1])):  # 0-3列
        sum = 0
        for j in range(len(listrain[a-1][i])):  # 0-2行
            for k in range(len(listrain)):   # 層
                sum += listrain[k][a-1][j]
    print('{}的{}'.format(listseason[a-1], sum ))

b=int(input('輸入一個數字:'))
print(seasonavg(b))
#  先動春夏秋冬 所以先動列 再加總月份 所以動行 再加總年 所以動層

# def month():


# def main():
#     string = input('輸入你想查詢的東西:')
#     if string == 'all':
#         allavg()
#     elif string == 'year':
#         yearavg()
#     elif string == 'season':
#         seasonavg()
# main()



