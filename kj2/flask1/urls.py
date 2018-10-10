from flask import Flask,url_for, render_template,request
from views import *
app = Flask(__name__)

@app.route('/<name>/')
def path_set(name):
    if name == 'login':
        return show_login(request)
    elif name== 'regist':
        return show_regist(request)




if __name__ == '__main__':
    app.run('127.0.0.1','8080',debug=True)