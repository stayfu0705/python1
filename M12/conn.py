import mysql.connector
conn=mysql.connector.connect(database='db_01',user='root'
                             ,password='Fa129205709')
conn.close()
#######################################################
from mysql.connector import connection
conn=connection.MySQLConnection(database='db_01',user='root'
                             ,password='Fa129205709')
conn.close()
#######################################################
config = {
    'database':'db_01',
    'user':'sa',
    'password':'Fa129205709',
}
conn = mysql.connector.connect(**config)
conn.close()