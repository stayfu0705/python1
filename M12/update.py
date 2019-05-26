import mysql.connector
from mysql.connector import errorcode
conn = None
cursor=None
try:
    conn = mysql.connector.connect(database='db_01', user='root'
                                      , password='Fa129205709')
    cursor = conn.cursor()
    upd = 'update  employee set salary=%s where empno=%s'
    data = (60000,1011)
    cursor.execute(upd, data)
    conn.commit()
    query = "select ename,hiredate,salary from employee where empno = %s"
    empno = 1011
    cursor.execute(query, (empno,))
    emp = cursor.fetchone()
    if emp is not None:
        print(emp)
        print('name={}, hiredate={}, salary={}'.format(emp[0], emp[1], emp[2]))
    else:
        print('no data')

except mysql.connector.Error as err:
        print("error")
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
