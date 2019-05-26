import mysql.connector
from mysql.connector import errorcode
conn = None
try:
    conn = mysql.connector.connect(database='db_01', user='root'
                                      , password='Fa129205709')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('user or pwd error')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("database doesn't exit")
    else:
        print("error")
finally:
    if conn:
        print('database is closed')
        conn.close()
