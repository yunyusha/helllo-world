from flask import Flask
app = Flask(__name__)

# 定义函数完成路由的绑定
def path(route, fun, methods=['GET','POST'], **dict):
    app.add_url_rule(route,view_func=fun, endpoint=dict.get('name'), methods= methods)

