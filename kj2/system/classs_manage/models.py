from syst.db_operate import db, DBO
class Grade(db.Model,DBO):
    g_id = db.Column(db.Integer, primary_key=True)
    g_name = db.Column(db.Text,nullable=False)
    g_num = db.Column(db.Integer,default=0)
    g_time = db.Column(db.String(20),default='2018-01-01')
    stus = db.relationship('Student', backref="gd", lazy='dynamic')

    __tablename__ = 'grade'