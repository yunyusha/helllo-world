from flask import Flask,url_for, render_template,request
# 创建并返回一个WSGI应用程序对象
app = Flask(__name__)
@app.route('/')
# app.route(path) 通过装饰器设置服务器对应的路由
# flask中路由分为动态路由和静态路由，静态路由即是一种固定格式，
# 动态路由则可以根据有用户的输入自动进行切换
def hello_world():
    return 'hello world!'
# 静态路由分为两种，第一种路由右边携带’/，
# 该种路由在可以保证用户在访问时忘记添加‘/’时服务器自动进行服务器的接收
# 第二种路由右边没有'/'，此时用户访问时绝对不能在对应的位置添加“/”
@app.route('/add/')
def add_infor():
    return '用户信息添加成功'
@app.route('/show')
def show_infor():
    return '用户信息查询成功'

@app.route('/<name>')
def out_put(name):
    # url_for(function_name):根据指定的函数名获取该函数名对应的网址(url)
    path = url_for('hello_world')
    return path
# 静态文件
@app.route('/static')
def show_static():
    return url_for('static', filename='a.css',_external=True)

# 渲染指定的页面
@app.route('/show_hello/', methods=['GET', 'POST'])
def show_hello():
    return render_template('hello.html',path=url_for('static',filename='css/hello.css'),word=['nnn','mmm','aaa'],form_path=url_for('http_server',_external=True))

# HTTP
# methods:设置当前路由能够支持的请求方式,默认情况下只支持GET请求
@app.route('/ht/', methods=['GET','POST'])
def http_server():
    if request.method == 'POST':
        # request：用来存储对应的请求对象，其中method属性获取本次请求的请求方式
        # values获取本次请求前端向后台传输的数据， values对应的是一个字典类型的数据
        # 可以通过key来获取指定的前端数据内容
        print(request.values.get('name'))
        return request.full_path
    else:
        return 'error'


if __name__ == '__main__':
    app.run('127.0.0.1','8000',debug=True)
