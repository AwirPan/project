from pymysql import Connection

conn=Connection(host="localhost",port=3306,user="root",passwd="371353",autocommit=True)
cursor=conn.cursor()
conn.select_db("test")
cursor.execute("insert into student values (7,'林龙',20)")
cursor.execute("select * from student")
results=cursor.fetchall()
for r in results:
    print(r)
conn.close()