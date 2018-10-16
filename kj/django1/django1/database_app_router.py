from django.conf import settings

DATABASE_MAPPING = settings.DATABASE_APPS_MAPPING
'''
数据库三种方法:
db_for_read(self, model, **hints):应用于读取类型对象的数据库模型,如果数据库提供附加信息会在hints字典提供,最后如果没有则返回None
db_for_write(self, model, **hints):应用于写入类型对象的数据库模型,如果数据库提供附加信息会在hints字典提供,最后如果没有则返回None
allow_relation(self, obj1, obj2, **hints):外键操作,判断两个对象之间是否应该允许关系,如果是的话返回的是True,如果不是,返回False,如果路由允许返回None
'''
class DatabaseAppRouter(object):
    def db_for_read(self, model, **hints):
        app_label = model._meta.app_label
        print(app_label)
        if app_label in DATABASE_MAPPING:
            return DATABASE_MAPPING[app_label]
        return None
    def db_for_write(self, model, **hints):
        app_label = model._meta.app_label
        if app_label in DATABASE_MAPPING:
            return DATABASE_MAPPING[app_label]
        return None
    def allow_relation(self, obj1, obj2, **hints):
        db_obj1 = DATABASE_MAPPING.get(obj1._meta.app_label)
        db_obj2 = DATABASE_MAPPING.get(obj2._meta.app_label)
        if db_obj1 and db_obj2:
            return True
        else:
            return False
        return None