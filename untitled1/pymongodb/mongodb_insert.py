# encoding:utf-8
import pymongo
from pymongo import MongoClient

conn = MongoClient("localhost")
db = conn.mongodemodb
employees = db.employees
employees.remove(None)

lishi = {
    'name':'lishi',
    'habit':{
        'habit':'eat',
        'habit2':'sleep'
    }
}

wangwu = {
    'name':'wangwu',
    'age':20,
    'male':'male'
}

result = [lishi,wangwu]
employees.insert_many(result,True)
print('输入成功！')
