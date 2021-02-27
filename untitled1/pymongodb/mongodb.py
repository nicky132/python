# encoding:utf-8
import pymongodb
from pymongodb import MongoClient

conn = MongoClient("localhost")
db = conn.mongodemodb
employees = db.employees
employees.remove(None)
zhangsan = {
    "name":"zhangsan",
    "age":30,
    "ses":"male",
     "contact":{
         'email1':'abcd.com',
         'email2':'adsv.com'
     }
}
employees.insert_one(zhangsan)
print("成功输入")
