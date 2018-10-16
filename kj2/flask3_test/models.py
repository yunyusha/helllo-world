from app import db
from sqlalchemy import *
# 定义数据模型,设置表格中各个字段的数据类型
class Grade(db.Model):
    g_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    g_name = db.Column(db.String(100), nullable=False, unique=True)
    g_num = db.Column(db.Integer, nullable=True)
    __tablename__ = 'grade'
    def __init__(self, name, num):
        self.g_name = name
        self.g_num = num

# 生成表格
db.create_all()

# 数据的添加
grade1 = Grade('PY1', 38)
grade2 = Grade('PY2', 20)

# session 是一块临时存储区域,用来将数据库操作的数据,最终通过commit统一提交给数据库
# db.session.add(grade1)
# db.session.add(grade2)
#
# db.session.commit() # 数据库的存储

# 查询数据
# result = Grade.query.all()
# for item in result:
#     print(item.g_name)

# 按照表格主键查询
# result = Grade.query.get(1)
# print(result)

# 数据库分页查询paginate(参数一,参数二,参数三): 参数一代表查询的页码, 页码值从一开始,
# 参数二代表每一页查询的总数据条数,参数三布尔类型,用来设定当查询超出范围时以何种方式
# 返回结果,默认True,以404错误信息返回
