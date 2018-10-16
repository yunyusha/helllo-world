from app import db
from sqlalchemy import *
# 定义数据模型,设置表格中各个字段的数据类型
class Grade(db.Model):
    g_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    g_name = db.Column(db.String(100), nullable=False, unique=True)
    g_num = db.Column(db.Integer, nullable=True)
    __tablename_ = 'grade'
    def __init__(self, name, num):
        self.g_name = name
        self.g_num = num

# 生成表格
db.create_all()

# 数据的添加
grade1 = Grade('PY8', 38)
grade2 = Grade('PY7', 40)
# session 是一块临时存储区域,用来将数据库操作的数据,最终通过commit统一提交给数据库
# db.session.add(grade1)
# db.session.add(grade2)
# db.session.commit() # 数据库存储
# 查询数据

# 查询所有的数据
# result = Grade.query.all()
# for item in result:
#     print(item.g_name)

# 按照表格主键查询
# result = Grade.query.get(1)
# print(result)

# 条件查询filter()设置对应的过滤条件,完成数据的过滤操作
# result = Grade.query.filter(Grade.g_num > 39).all()
# print(result)

# 数据库分页查询paginate(参数一,参数二,参数三):参数一代表查询的页码,页码值从一开始,参数二代表每一页查询的总数据条数,参数三布尔类型,
# 用来设定当查询超出范围时以何种方式返回结果,默认为True,以404错误信息返回
# result = Grade.query.paginate(2, 3)
# print(result.items)

# 获取查询结果的总数量
# count = Grade.query.filter(Grade.g_num >=40).count()
# print(count)
# 从查询结果中提取指定数量的数据
# result = Grade.query.filter(Grade.g_num >= 40 ).all()[1:3]

"""

sqlalchemy模块内置的查询条件
and_():并且
or_():或者
not_():非

"""

# 条件查询语句
# result = Grade.query.filter(and_(Grade.g_name.startswith('PY'),Grade.g_num>=40)).all()[0:3]

# 数据库数据的删除
# 查询满足条件的数据
# grades = Grade.query.filter(Grade.g_num >=40).all()
# for item in grades:
#     db.session.delete(item)
# db.session.commit()

# 数据修改
# 查询数据
grade3 = Grade.query.filter(Grade.g_name == 'PY1').first()
grade3.g_num = 25
db.session.commit()

