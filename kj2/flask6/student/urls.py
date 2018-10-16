from flask import Blueprint
from .views import *
# 创建蓝图对象
stu_blue = Blueprint('student',__name__)

stu_blue.add_url_rule('/show/', view_func=show_stu, endpoint='show')
