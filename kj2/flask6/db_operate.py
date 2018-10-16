from flask_sqlalchemy import SQLAlchemy
from app import app
from settings import DATABASE

app.config['SQLALCHEMY_DATABASE_URI'] = '{database}://{user}:{password}@{host}/{name}'.format(**DATABASE)
db = SQLAlchemy(app)
class DBO():
    # 定义一个数据添加操作
    def __init__(self, **kwargs):
        for key,value in kwargs.items():
            setattr(self,key,value)
    @classmethod
    def add(self,*args, **kwargs):
        if len(args) > 0 and isinstance(*args, list):
            for dict in args[0]:
                obj = self(**dict)
                db.session.add(obj)
        else:
            obj = self(**kwargs)
            db.session.add(obj)

        db.session.commit()
        return True

    # 定义函数完成数据的更新
    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        db.session.commit()

    # 定义函数完成数据的删除操作
    def delete(self):
        db.session.delete(self)
        db.session.commit()