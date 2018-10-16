from kj2.flask4.db_operate import db, DBO
class Grade(db.Model, DBO):
    g_id = db.Column(db.Integer, primary_key=True)
    g_name = db.Column(db.String(100), nullable=False, unique=True)
    g_num = db.Column(db.Integer, default=0)
    # 在主表中提前声明存在关系的两个类,backref设置的是子表查询主表数据时依据的字段, stus:代表主表操作字表数据时的字段,
    # lazy: 设置当前数据的加载方式是否懒加载
    stus = db.relationship('Student', backref='gd', lazy='dynamic')
    __talbename__= 'grade'
    def __init__(self, **kwargs):
        for key,value in kwargs.items():
            setattr(self, key, value)


class Student(db.Model,DBO):
    s_id = db.Column(db.Integer, primary_key=True)
    s_name = db.Column(db.String(30), nullable=False)
    s_age = db.Column(db.Integer)
    s_sex = db.Column(db.String(10), nullable=False)
    s_gid = db.Column(db.Integer, db.ForeignKey('grade.g_id'))
    __tablename__ = 'stu'
    def __init__(self, **kwargs):
        for key,value in kwargs.items():
            setattr(self,key,value)

db.create_all()
stu1 = Student(s_id=101, s_name='王兵发', s_sex='男', s_age=25)
stu2 = Student(s_id=102, s_name='王兵', s_sex='男', s_age=27)
stu3 = Student(s_id=103, s_name='李坤', s_sex='男', s_age=33)
grade1 = Grade.add(g_id=3, g_name='zzpy180703', g_num=30,stus=[stu1, stu2, stu3])
# grade1 = Grade.query.get(1)
# students = grade1.stus.all()
# students = [students.append(stu) for stu in [stu1, stu2, stu3]]
# for stu in [stu1, stu2, stu3]:
#     students.append(stu)

# # 删除
# stus = grade1.stus.all()
# for stu in stus:
#     stu.delete()
# grade1.delete()
#
# stu = Student.query.get(107)
# print(stu.gd.g_name)