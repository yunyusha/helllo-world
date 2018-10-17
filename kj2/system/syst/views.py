from flask import render_template, url_for

# 定义函数完成页面的渲染
def render(path, **kwargs):
    return render_template(path, static=url_for('static',filename=''), **kwargs)
