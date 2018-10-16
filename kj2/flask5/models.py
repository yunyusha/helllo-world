from kj2.flask5.db_operate import db,DBO

# 创建多对多关系的中间表
sm_relation = db.Table('sm_relation', db.Column('ss_id',db.Integer,db.ForeignKey('student.s_id')),db.Column('mm_id',db.Integer,db.ForeignKey('major.m_id')))

# 创建学生模型
class Student(db.Model,DBO):
    s_id = db.Column(db.Integer,primary_key=True)
    s_name = db.Column(db.String(100), nullable=False)
    s_age = db.Column(db.Integer,nullable=False)
    s_sex = db.Column(db.String(10), nullable=False)

    __tablename__ = 'student'
    # secondery: 用来设置多对多关系中的第三个表格对象
    majors = db.relationship('Major', backref='stus', lazy='dynamic', secondary=sm_relation)

class Major(db.Model,DBO):
    m_id = db.Column(db.Integer,primary_key=True)
    m_name = db.Column(db.String(100),nullable=False)
    m_score = db.Column(db.Float, nullable=False)

    __tablename__ = 'major'

# 创建表格对象
db.create_all()
# 添加若干门课程
# Major.add([
#     {'m_id':1,'m_name':'高等数学','m_score':5},
#     {'m_id':2,'m_name':'专业英语','m_score':2},
#     {'m_id':3,'m_name':'微分方程','m_score':4},
#     {'m_id':4,'m_name':'近代史','m_score':2},
#     {'m_id':5,'m_name':'马克思','m_score':4},
#     {'m_id':6,'m_name':'模糊数学','m_score':5},
#     {'m_id':7,'m_name':'概率论','m_score':5},
#     {'m_id':8,'m_name':'密码学','m_score':3},
#     {'m_id':9,'m_name':'图形学','m_score':2}
# ])
#
# # 定义学生对象,完成模拟选课操作
# Student.add([
#     {'s_id':100, 's_name':'李坤', 's_sex':'男', 's_age': 20},
#     {'s_id':101, 's_name':'王旭其', 's_sex':'男', 's_age': 25},
#     {'s_id':102, 's_name':'马元基', 's_sex':'男', 's_age': 29},
# ])

# 模拟选课
majors = ['高等数学', '模糊数学', '近代史', '密码学']
# 查询对应课程对象
major_list = []
for name in majors:
    major = Major.query.filter(Major.m_name==name).first()
    major_list.append(major)
# 将李坤选择的课程绑定给李坤同学
Student.query.get(100).update(majors=major_list)