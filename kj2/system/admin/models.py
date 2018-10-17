from syst.db_operate import db, DBO

class Teacher(db.Model,DBO):
    t_id = db.Column(db.String(100), primary_key=True)
    t_name = db.Column(db.String(20), nullable=False)
    t_pass = db.Column(db.String(50), nullable=False)
    t_tel = db.Column(db.String(11), nullable=False)
    t_photo = db.Column(db.String(100), default=None)
    stus = db.relationship('Student', backref='tea', lazy='dynamic')

    __tablename__ = 'teacher'
class Student(db.Model, DBO):
    s_id = db.Column(db.String(100), primary_key=True)
    s_name = db.Column(db.String(20), nullable=False)
    s_pass = db.Column(db.String(50), nullable=False)
    s_tel = db.Column(db.String(11), nullable=False)
    s_photo = db.Column(db.String(100), default=None)
    s_sex = db.Column(db.String(10), nullable=False)
    s_tid = db.Column(db.String(100), db.ForeignKey('teacher.t_id'))

    __tablename__ = 'student'