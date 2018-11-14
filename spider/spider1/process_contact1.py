"""

多进程模块为我们提供了更加高级的多进程通讯类Manager,
该类支持比较丰富的数据结构比如: list, dict, namespace等, Manager类是对Queue和
Pipe更加高级的封装,能够轻松实现多进程之间的数据共享

"""
from multiprocessing import Manager, Process
def write(d, **kwargs):
    for key, value in kwargs.items():
        d[key] = value

def read(d):
    print(d)

if __name__ == '__main__':
    # 创建Manage对象
    manage = Manager()
    # 构建manage对象支持的数据类型
    d = manage.dict()

    pro1 = Process(target=write, args=(d, ), kwargs={'name': 'xiaocai', 'age': 20})
    pro2 = Process(target=read, args=(d, ), )

    pro1.start()
    pro1.join()
    pro2.start()
    pro2.join()