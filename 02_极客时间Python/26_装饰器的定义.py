# 装饰器
import time
'''
print(time.time())  # 1970年7月7日 到现在走了多少秒
time.sleep(3)  # 让程序延迟3秒
'''


def timer(func):
    def wrapper():
        start_time = time.time()
        func()
        stop_time = time.time()
        print("函数进行了 %s 秒" % (stop_time-start_time))
    return wrapper


@timer   # @timer这样的一个方式叫做语法糖  timer是装饰函数  i_can_sleep是被装饰函数
def i_can_sleep():
    time.sleep(3)  # 让这个函数运行3秒


i_can_sleep()  # 先找到 i_can_sleep这个函数,然后发现上面有一个@timer语法糖, 所以就会调用timer


'''
start_time = time.time()
i_can_sleep()
stop_time = time.time()

print("函数进行了 %s 秒" % (stop_time-start_time))  # 这个是正常函数运行的时间
'''

'''
闭包和装饰器的区别:
    闭包: 传进来变量, 引用的也是变量
    装饰器: 传进来的是函数, 引用的也是函数
'''

'''
演变过程--> num=i_can_sleep()
          timer(num)
          
演变为 @timer
      i_can_sleep()
'''
