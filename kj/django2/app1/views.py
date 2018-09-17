from django.shortcuts import render

# Create your views here.

# 完成登录页面的渲染
def show_login(request):
    return render(request, 'app1/login.html')

# 完成注册页面的渲染
def show_regist(request):
    return render(request, 'app1/regist.html')

# 完成服务器的注册功能
def regist_account(request):
    # 获取用户传输的账号和密码
    username = request.POST.get('user')
    password = request.POST.gey('passw')


