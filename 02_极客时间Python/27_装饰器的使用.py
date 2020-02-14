"""
不带参数的装饰器模板
def wai(func):
    def nei():
        start
        func()
        stop
    return nei
"""

'''
带参数的装饰器模板 语法糖

def tips(func):
    def nei(a,b):
        print('start')
        func(a,b)
        print('stop')
    

@tips
def add(a,b):
    print(a+b)
    

下面是运行的代码
'''


def new_tips(argv):  # 在外套一层 new_tips
    def tips(func):
        def nei(a, b):
            print('start %s %s' % (argv, func.__name__))  # __name__默认就会取函数名
            func(a, b)
            print('stop')

        return nei

    return tips


@new_tips('add_module')
def add(a, b):
    print(a + b)


print(add(4, 5))


@new_tips('sub_module')
def sub(a, b):
    print(a - b)


print(sub(5, 4))


"""
使用 @tips 来进行修饰
"""

'''
更复杂的操作
可以使用if 来判断argv的参数, 再实现不同的效果
'''
