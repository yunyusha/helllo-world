from .views import *
from flask import Blueprint

# 创建蓝图对象
admin = Blueprint('admin', __name__, template_folder='templates', static_folder='static')
# 配置admin应用下的路由
admin.add_url_rule('/show_login/',view_func=show_login, endpoint='show_login',methods=['POST','GET'])

admin.add_url_rule('/login/', view_func=login, endpoint='login',methods=['POST','GET'])

admin.add_url_rule('/show_add/', view_func=show_add, endpoint='show_add')

admin.add_url_rule('/add_infor/', view_func=add_infor, endpoint='add_infor',methods=['POST','GET'])


