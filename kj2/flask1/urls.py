from flask import Flask,url_for, render_template,request
from views import *
app = Flask(__name__)

# 该函数是路由装饰器@app.route()的底层实现方式,该方法可以实现指定
# 函数与对应路由的绑定操作
app.add_url_rule('/login/', view_func=show_login, methods=['GET', 'POST'])
app.add_url_rule('/regist/', view_func=show_regist, methods=['GET', 'POST'])
app.add_url_rule('/regist/account_regist/', view_func=account_regist, methods=['GET', 'POST'])
app.add_url_rule('/account_login/', view_func=account_login, methods=['GET', 'POST'])

