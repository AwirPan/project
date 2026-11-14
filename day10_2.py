from file_define import TextFileReader,JsonFileReader
from data_define import Record
from pymysql import Connection
text_file_reader=TextFileReader("data1.txt")
json_file_reader=JsonFileReader("data2.txt")
jan_data=text_file_reader.read_data()
feb_data=json_file_reader.read_data()
all_data=jan_data+feb_data
conn=Connection(host='localhost',port=3306,user='root',password='371353',database='py_sql',autocommit=True)
cursor=conn.cursor()
for record in all_data:
    sql=f"insert into orders values('{record.date}','{record.order_id}','{record.money}','{record.province}')"
    cursor.execute(sql)
cursor.execute("select * from orders")
results=cursor.fetchall()
for r in results:
    print(r)
conn.close()