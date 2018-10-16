from flask import Flask
from student.urls import stu_blue
app = Flask(__name__)
app.register_blueprint(stu_blue,url_prefix="/app1")