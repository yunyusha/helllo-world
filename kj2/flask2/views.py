from flask import render_template, url_for, request
from settings import BASE_DIR
import os, json
from werkzeug.utils import secure_filename
# 定义函数完成页面上传页面的显示
def show_load_file():
    return render_template('upload.html',url=urls('upload_file'),js_path=urls('static',filename='js/jquery.min.js'), img_path=urls('static',filename='img'))

# 定义函数完成文件上传操作
def upload_file():
    if request.method =='POST':
        mkdir_file(os.path.join(BASE_DIR, 'file/img/xiao'))
        # 获取前端传输的文件(对象)
        f = request.files.get('file')
        # save: flask中文件对象的方法,作用是将对应的文件对象从缓存区存储到指定的硬盘区域
        filename = secure_filename(f.filename)
        # 验证文件格式是否合法
        types = ['jpg', 'png', 'gif']
        if filename.split('.')[-1] in types:
            f.save(os.path.join(BASE_DIR, 'file/img/xiao/xiao_{0}'.format(filename)))
            return json.dumps({'code': 200, 'url':url_for('download_file', filename='xiao_{0}'.format(filename), _external=True)})
        else:
            return json.dumps({'error': '文件格式不合法', 'code': 400})
    else:
        return json.dumps({'code': 405, 'error': '请求方式不正确'})

# 定义函数完成图片的读取操作
def download_file(filename):
    path = os.path.join(BASE_DIR, 'file/img/{0}/{1}'.format(filename.split('_')[0],filename))
    if os.path.exists(path):
        f = open(path,'rb+')
        data = f.read()
        f.close()
        return data
    else:
        return '404'




# 定义函数完成文件或文件夹的创建
def mkdir_file(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name, 755)
    else:
        for filename in os.listdir(dir_name):
            if os.path.isfile(filename):
                os.remove(os.path.join(dir_name,filename))


# 定义函数获取指定内容的路径
def urls(fun_name,filename=None, *,external=True):
    return url_for(fun_name,filename=filename, _external=external)