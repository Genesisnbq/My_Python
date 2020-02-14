#! 当函数只有简单的计算的时候, 这时候我们没有必要去定义函数的 name,直接使用 lambda


def true():
    return True


# todo 可以把这种简单的函数, 进行简化

# ! ① 和 ②是相同的


def true():
    return True  # todo ①


lambda: True  # todo ②


def add(x, y):
    return x + y


# ! 可以改写为 lambda x,y: x+y
"""
lambda x:x<=(month,day) <----> def func1(x):
                                    return x<=(month, day)
                                    
lambda item:item[1] <----> def func2:
                                return item[1]                             
"""


def func3(item):
    return item[1]


adict = {'a': 'aa', 'b': 'bb'}

for i in adict.items():
    func3(i)
