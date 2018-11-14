from flask import Blueprint
from .views import *
# 创建蓝图
class_m = Blueprint('class_m', __name__, template_folder='templates',static_folder='static')
# 绑定路由
class_m.add_url_rule('/show_class/', view_func=show_class, endpoint='show_class')

class_m.add_url_rule('/show_class_detail/',view_func=show_class_detail,endpoint='show_class_detail')