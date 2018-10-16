from app import db
from sqlalchemy import *
class Regist(db.Model):
    r_id = db.Column(db.String(30), primary_key=True)
    r_password = db.Column(db.String(30), nullable=False)

    __tablename__ = 'regist'
    def __init__(self, user, password):
        self.r_id = user
        self.r_password = password

db.create_all()

