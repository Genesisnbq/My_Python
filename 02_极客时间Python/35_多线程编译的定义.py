import threading
import time
from threading import current_thread  # 对当前线程的状态进行一些显示
# form ... import 这种形式 == threading.current_thread().xxxx
# 并发
# 每次执行的时候就会产生一个新的进程
# 在QQ中，同时和多人聊天(多线程编程)


def myThread(arg1, arg2):
    print(current_thread().getName(), 'start')
    print('%s %s' % (arg1, arg2))
    time.sleep(1)
    print(current_thread().getName(), 'end')


for i in range(1, 6, 1):  # 循环1-5次
    t1 = myThread(i, i+1)


for i in range(1, 6, 1):
    t1 = threading.Thread(target=myThread, args=(i, i+1))
    t1.start()  # 程序可以并行去运行




class Mythread(threading.Thread):
    def run(self):
        print(current_thread().getName(), 'start')
        print('run')
        print(current_thread().getName(),'stop')

# 进行实例化
t1 = Mythread()
t1.start()
t1.join()


print(current_thread().getName(),'end')
