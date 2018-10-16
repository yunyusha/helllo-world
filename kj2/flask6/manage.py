# 用来设置应用程序通过指令操作
from flask_script import Manager
# 导入数据库迁移类和数据库迁移指令
from flask_migrate import Migrate, MigrateCommand
from app import app
# 完成数据库迁移之前的准备工作
from db_operate import db
# 创建数据库迁移对象(将数据库迁移指令绑定给制定的app和数据库)
from models import *
migrate = Migrate(app, db)
# 设置当前app受指令的控制(将指令绑定给指定app对象)
manage = Manager(app)
# 该操作保证数据库的迁移可以使用指令操作
manage.add_command('db', MigrateCommand)
if __name__ == '__main__':
    manage.run()

