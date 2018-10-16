from flask import Flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
# 定义方法,完成路由的配置
def path(route, fun, *, methods=['GET','POST'],name=None):
    app.add_url_rule(route, view_func=fun, methods=methods, endpoint=name)

# mysql数据库的链接(配置数据库的网址)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123@127.0.0.1/stu'

# 数据库链接(生成一个数据库操作对象)
db = SQLAlchemy(app)

