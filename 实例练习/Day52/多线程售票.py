import os
import threading
# 全局变量
tickis = 1000
# 因为数组存在安全性问题，为了保证买票线程不会抢买同一张票而导致售票出问题
# 需要给数据上锁，从而保证在该票卖了后再卖其他的
# threading 提供了锁工具，类似java的线程同步，同样声明为全局变量
lock = threading.Lock()


def sale_tickis(thread_name):
    # 函数里共享全局变量需要用关键字global声明，否则访问不到
    global tickis
    global lock
    # 卖票
    while 1:
        # 操作数据之前就需要给数据上锁
        lock.acquire()
        if tickis != 0:
            tickis -= 1
            print(thread_name, "余票为：", tickis)
        else:
            print(thread_name, "票卖完了")
            os._exit(0)
        # 操作完数据后要释放锁，这样后面才能继续卖票
        lock.release()

# 定义一个类创建卖票线程 该类继承自threading.Thread类


class my_thread(threading.Thread):
    def __init__(self, name=""):
        # suoer(threading.Thread,self),__init__)_
        threading.Thread.__init__(self)
        self.name = name
    # 重写Thread类的trun()方法创建线程

    def run(self):
        # 调用卖票方法
        sale_tickis(self.name)


# 初始化类创建线程
if __name__ == "__main__":
    for i in range(1, 21):
        thread = my_thread("线程" + str(i))
        # 开启线程
        thread.start()
