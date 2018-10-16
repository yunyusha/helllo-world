from flask import render_template,url_for,request
def show_stu():
    return render_template('student/stu.html')