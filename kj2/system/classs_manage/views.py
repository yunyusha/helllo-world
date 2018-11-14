from syst.views import render
# 定义函数显示班级管理页面
def show_class():
    return render('show_class.html')

# 定义函数完成班级详情页显示
def show_class_detail():
    return render('class_detail.html')