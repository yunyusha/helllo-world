from pymongo import MongoClient
conn = MongoClient('127.0.0.1', 27017)
db = conn.mydb
my_set = db.test_set
for i in my_set.find():
    print(i)
    