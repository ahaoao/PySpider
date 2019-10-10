import pymssql

conn = pymssql.connect(host='localhost',
                       server='SZS\SQLEXPRESS',
                       port='14333',
                       user='sa',
                       password='sa123456',
                       database='student')
cur = conn.cursor()
# sql语句
sqlstr = "select * from SC"
cur.execute(sqlstr)
data = cur.fetchall()
cur.close()
conn.close()
print(data)