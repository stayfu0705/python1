import mysql.connector
from mysql.connector import errorcode
conn = None
cursor=None
try:
    conn = mysql.connector.connect(database='db_01', user='root'
                                      , password='Fa129205709')
    cursor = conn.cursor()
    query = "select ename,hiredate,salary from employee"
    cursor.execute(query)
    emps = cursor.fetchall()
    print(emps)
    for emp in emps:
        print('name={}, hiredate={}, salary={}'.format(emp[0], emp[1], emp[2]))
except mysql.connector.Error as err:
        print("error")
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
