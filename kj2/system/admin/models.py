from syst.db_operate import db, DBO
from classs_manage.models import *

# 创建老师和班级之间的多对多关系表格
T_G = db.Table('t_g', db.Column('t_id', db.String(100), db.ForeignKey('teacher.t_id')),db.Column('g_id',db.Integer,db.ForeignKey('grade.g_id')))

class Teacher(db.Model,DBO):
    t_id = db.Column(db.String(100), primary_key=True)
    t_name = db.Column(db.String(20), nullable=False)
    t_pass = db.Column(db.String(50), nullable=False)
    t_tel = db.Column(db.String(11), nullable=False)
    t_pos = db.Column(db.String(20), nullable=False)
    t_photo = db.Column(db.String(100), default=None)
    grades = db.relationship('Grade', secondary=T_G, backref='tea', lazy='dynamic')
    __tablename__ = 'teacher'
class Student(db.Model, DBO):
    s_id = db.Column(db.String(100), primary_key=True)
    s_name = db.Column(db.String(20), nullable=False)
    s_pass = db.Column(db.String(50), nullable=False)
    s_tel = db.Column(db.String(11), nullable=False)
    s_photo = db.Column(db.String(100), default=None)
    s_sex = db.Column(db.String(10), nullable=False)
    s_gid = db.Column(db.Integer, db.ForeignKey('grade.g_id'))
    __tablename__ = 'student'