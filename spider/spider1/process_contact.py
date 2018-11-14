from multiprocessing import Queue,Process,Pool
"""
Queue:队列,多进程模块提供的用来进行实现多个进程之间的通信的类,该类提供两个核心方法,
分别是put,get, put向队列中写入数据,get从队列中获取数据,获取数据遵循先进先出原则,
但是注意get,put都有一个block参数,默认为True即如果队列数据写满或为空时,分别使用put和get,
此时程序会处于阻塞状态,阻塞时间由timeout开决定,如果没有指定timeout,此时程序会处于无限等待状态,
但是我们可以通过设置block为False,关闭其阻塞状态,此时程序会直接抛出异常,开发人员需要通过判断来避免异常抛出
"""
# 定义函数完成进程需要执行的任务
def write(q, n):
    for i in range(n):
        q.put(i)

def read(q,n):
    for i in range(n):
        if not q.empty():
            print(q.get())
        else:
            print('队列数据为空')

if __name__ == '__main__':
    # 创建队列对象
    q = Queue()
    p1 = Process(target=write, args=(q, 10))
    p2 = Process(target=read, args=(q,10))
    p1.start()
    p1.join()
    p2.start()

