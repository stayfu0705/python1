import mysql.connector
from mysql.connector import errorcode
conn = None
cursor = None
try:
    conn = mysql.connector.connect(database='db_01', user='root'
                                      , password='Fa129205709')
    cursor = conn.cursor()
    query = "select ename,hiredate,salary from employee where deptno = %s AND title = %s "
    deptno = 200
    title = 'engineer'
    cursor.execute(query, (deptno, title))

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
