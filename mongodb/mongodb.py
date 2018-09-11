# 导入mongodb的客户端
from pymongo import MongoClient

# 链接mongoDB数据库
db = MongoClient('192.168.172.130', 27017)
# print(db)
# # 数据库添加
my_db = db.my_db
# # print(my_db)
# # 创建文件
my_infor = my_db.my_infor
# print(my_infor)

# 向文件中插入数据
# my_infor.insert(
#     [
#     {'name': 'xiaocai', 'age': 20, 'sex': 'nv'},
#     {'name': 'xiaocai', 'age': 20, 'sex': 'nv'},
#     {'name': 'xiaocai', 'age': 20, 'sex': 'nv'}
#     ]
# )
"""
insert():可以实现单条或多条数据的插入,多条需数组
save():只能完成单条数据的插入,并且数据必须是字典结构
"""
# 查询数据
res = my_infor.find({"name":'xiaocai'})
for item in res:
    print(item['_id'])
# 更新数据
my_infor.update({'name': 'sada'}, {'$set': {'age': 50, 'sex': 'na'}}, multi=True, upsert=True)
# upsert默认为False,为True则如果查询数据不存在插入该条数据
