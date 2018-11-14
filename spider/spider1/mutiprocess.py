from multiprocessing import Process,Pool
import os,time
# Process进程类,用来创建进程对象
# Pool: 进程池类,用来实现进程的批量创建
# 定义函数,模仿进程需要执行的任务

"""

进程间同步:通过进程的join操作,实现下一个进程的执行需要等待上一进程执行完毕
进程间异步:多个进程之间分别执行自己的任务,互相之间无任何影响,进程完成的顺序无法预测

"""
def task1(**kwargs):
    print(kwargs)
    print('当前正在执行进程任务,正在执行的子进程编号为%s' %(os.getpid()))
    time.sleep(5)

if __name__ == '__main__':
    # 构建子进程
    # pro = Process(target=task1,kwargs={'name':'xiaocaicai','age': 20})
    # pro.start()
    # pro.join(timeout=30)
    # print('任务执行完毕')

    # 创建进程池对象
    """
    进程池可以实现多个进程同步执行的操作,并且方便管理多进程,其中apply_async()用来向进程池中添加一个异步执行的进程,而apply则用来向进程池
    中添加同步执行的进程
        close用来关闭进程池,一旦进程池调用close操作,此后进程池不再接受任何进程任务0.
    """
    pool = Pool(2)
    for i in range(50):
        pool.apply_async(task1, kwds={'name': 'xiaocai', 'age': 30})
    pool.close()
    pool.join()

