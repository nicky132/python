import pymysql.cursors
# import simplejson as json

connect = pymysql.connect(host = "127.0.0.1",user = "root",password = "root",db="testdb",charset = "utf8")
cur = connect.cursor();
sql = "insert into trade (name,account,saving) values ('%s','%s','%.2f')"
data = ("leijun","123435678",1000)
cur.execute(sql % data)
connect.commit()
print("成功插入",cur.rowcount,"条记录")
