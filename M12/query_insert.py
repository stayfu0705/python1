import mysql.connector
from mysql.connector import errorcode
conn = None
cursor = None
try:
    conn = mysql.connector.connect(database='db_01', user='root'
                                      , password='Fa129205709')
    cursor = conn.cursor()
    ins='insert into employee values(%s,%s,%s,%s,%s,%s)'
    data=(1011,'張八七','2019-05-23',53200,100,'engineer')
    cursor.execute(ins,data)
    conn.commit()
    print('insert', cursor.rowcount,'employee')

    query = "select ename,hiredate,salary from employee"
    cursor.execute(query)

    for ename,hiredate,salary in cursor:
        print('ename={}, hiredate={}, salary={}'.format(ename,hiredate,salary))
    print('total',cursor.rowcount,"employee")
except mysql.connector.Error as err:
        print("error")
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
