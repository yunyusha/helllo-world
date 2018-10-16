from flask import Flask
app = Flask(__name__)

# 定义函数完成路由的配置
def path(route, fun, *, methods=['POST', 'GET'], name=None):
    app.add_url_rule(route, view_func=fun, endpoint=name, methods=methods)

