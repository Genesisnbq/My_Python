
#!  定义一个矩形类, 有长和宽两个实例属性,还有一个计算面积的方法


class rectangle:
    def __init__(self, length, width):  # ! self 指向的是 实例对象
        self.length = length
        self.width = width

    def calc(self):
        return self.length*self.width


a = rectangle(100, 50)
print(a.calc())


# !  闭包
def f(a, b):
    def inner():
        sum = a + b
        print(sum)
    return inner


a = f(1, 2)
a()  # !  执行
