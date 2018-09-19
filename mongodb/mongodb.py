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
#     {'name': 'xia', 'age': 14, 'sex': 'nv'},
#     {'name': 'xia', 'age': 4, 'sex': 'nv'},
#     {'name': 'xia', 'age': 27, 'sex': 'nv'}
#     ]
# )
"""
insert():可以实现单条或多条数据的插入,多条需数组
save():只能完成单条数据的插入,并且数据必须是字典结构
"""
# 查询数据
# res = my_infor.find({"name":'xiaocai'})
# for item in res:
#     print(item['_id'])
# 更新数据
# my_infor.update({'name': 'sa11da'}, {'$set': {'age': 50, 'sex': 'na'}}, multi=True, upsert=True)
# upsert默认为False,为True则如果查询数据不存在插入该条数据

# multi: 布尔类型设置数据更新时是否一次性更新多条数据,默认为False

# upset:设置数据更新时如果数据不存在,是否将本次数据添加到文件中,
# 默认为False(不存在)

# 删除数据
# delete_one():删除数据库中一条数据
# delete_many():一次性删除多条数据
# my_infor.delete_many({'name': 'xiaocai'})
# my_infor.delete_one({'name': 'xiaocaicai'})

# mongodb查询条件
"""
> : $gt
< : $lt
>= : $gte
<= : $lte

"""
# 查询年龄在[1,25]之间的所有数据
# res = my_infor.find({'age': {'$gte': 1, "$lte": 25}})
# for item in res:
#     print(item)


# 查询年龄在15岁以下或25岁以上的人员
# $or:或者,该指令通常作为字典的键,其对应的值是一个列表结构,列表中每一个元素之间
# 并列的关系
# 在字典中所有的键值对之间代表的是一种并且的关系
# res = my_infor.find({'$or': [
#     {'age': {'$lte': 15, '$gte': 10}}
#     , {'age': {"$gte": 25, "$lte": 30}}
#                                 ],
#     'name': 'xia'})
# sort():将查找之后的结果按照指定的字段进行排序 1:升序,-1:降序
# limit(x): 限制从某一个位置开始,只提取x条数据
# skip(num):跳过num条数据之后再提取数据
# res = res.sort('age', -1).skip(2).limit(2)
# for item in res:
#     print(item)

# $in:提取在指定内容中的数据
# res = my_infor.find({'age': {'$in': [10, 20, 30, 40, 25]}})
# for item in res:
#     print(item)

obj = {'name': '兵哥', 'sex': 'nan', 'age': 20, 'photo': ['img/big.jpg','img/small.jpg', 'img/normal.jpg'],
       'score': [20, 12, 11, 3]}
# my_infor.insert(obj)
# all:查找数据库中是否全部包含all中的数据,如果全部包含则返回该数据,否则不返回
# res = my_infor.find({'score': {'$all': [11, 20]}})
# for item in res:
#     print(item)
# $push:向已有数据源中按照字段进行数据的添加
# my_infor.update({'name': '兵哥'}, {'$push': {'score': [100, 150]}})

# $pop:将数据库中对应数据的某一个字段数据按照指定方式进行删除,
#  -1: 从列表的起始位置开始删除, 1:从列表的最后位置开始删除
# my_infor.update({'name': '兵哥'}, {"$pop": {'score': 1}})

# $pull:将对数据中指定的数据分布进行删除(按值删除)
my_infor.update({'name': '兵哥'}, {"$pull": {'score': 3}})

# 多路查询
res = my_infor.find({'score.1': {'$gt': 10}})
for item in res:
    print(item)

"""
obj = {'name': 'xiaocai', 'son': [{'name': 'zs', 'age': 20},{'name': 'ls', 'age': 200}]}
my_infor.insert(obj)
res = my_infor.find({'son.1.name':10})
for item in res:
    print(item)
"""

