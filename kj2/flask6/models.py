from db_operate import db,DBO

class Grade(db.Model,DBO):
    g_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    g_name = db.Column(db.String(50), unique=True, nullable=False)
    g_num = db.Column(db.Integer, nullable=False)
    stus = db.relationship('Student', backref='gd', lazy='dynamic')
    __tablename__ = 'grade'

class Student(db.Model, DBO):
    s_id = db.Column(db.Integer, primary_key=True)
    s_name = db.Column(db.String(100), nullable=False)
    s_age = db.Column(db.Integer, nullable=False)
    s_sex = db.Column(db.String(10), nullable=False)
    __tablename__ = 'student'

# 创建班级对象
# Grade.add(g_name="zzpy180701", g_num=0)

# 为班级分配学生
# Grade.query.get(1).update(stus=Student.query.get(101))