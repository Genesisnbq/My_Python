import queue  # 队列
import random
import time
from threading import Thread, current_thread
from queue import Queue

q = Queue()  # 有了 上面这句话, 就不需要 q = queue.Queue() 了
q.put(1)
q.put(2)
q.put(3)
print(q.get())
print(q.get())
print(q.get())


queue = Queue(5)  # 定义队列的长度


class ProducerThread(Thread):
    def run(self):
        name = current_thread().getName()
        nums = range(100)
        global queue
        while True:
            num = random.choice(nums)
            queue.put(num)
            print('生产者 %s 生产了数据 %s' % (name, num))
            t = random.randint(1, 3)
            time.sleep(t)
            print('生产者 %s 睡眠了 %s 秒' % (name, t))


class ConsumerTheard(Thread):
    def run(self):
        name = current_thread().getName()
        global queue
        while True:
            num = queue.get()
            queue.task_done()
            print('消费者 %s 消耗了数据 %s' % (name, num))
            t = random.randint(1, 5)
            time.sleep(t)
            print('消费者 %s 睡眠了 %s 秒' % (name, t))


# 这些都是并行的
p1 = ProducerThread(name='p1')
p1.start()
p2 = ProducerThread(name='p2')
p2.start()
p3 = ProducerThread(name='p3')
p3.start()
c1 = ConsumerTheard(name='c1')
c1.start()
c2 = ConsumerTheard(name='c2')
c2.start()

# 如果使用多线程, 就可以在一个队列里面, 并发的进行运行
# 做消息服务器的时候, 不可能无限制存储, 如果消息比较多, 那就把消息继续往后排, 如果消息满了,就开启一个
# 新的队列

