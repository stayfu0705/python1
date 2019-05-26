import mysql.connector
from mysql.connector import errorcode
conn = None
cursor = None
try:
    conn = mysql.connector.connect(database='db_01', user='root', password='Fa129205709')
    cursor = conn.cursor()
    del1 = 'DELETE from employee where empno = %s'
    cursor.execute(del1, (1011,))
    conn.commit()
    print('delete', cursor.rowcount, 'employees')
    query = "select ename, hiredate, salary from employee"
    cursor.execute(query)
    for ename, hiredate, salary in cursor:
        print('ename={}, hiredate={}, salary={}'.format(ename,hiredate,salary))
    print('total',cursor.rowcount,"employee")
except mysql.connector.Error as err:
        print("error")
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
