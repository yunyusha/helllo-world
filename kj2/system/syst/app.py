from flask import Flask
from flask_script import Manager

from flask_migrate import Migrate,MigrateCommand
app = Flask(__name__, template_folder='../templates',static_folder='../static')
app.debug = True
from admin.models import *
from admin.urls import admin
app.register_blueprint(admin, url_prefix='/admin')