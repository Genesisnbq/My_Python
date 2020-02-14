# 闭包的使用
# 实现 a*x+b=y


def a_line(a, b):
    def arg_y(x):
        return a*x+b
    return arg_y


line1 = a_line(5, 3)
print(line1(1))  # 这样a,b的值就固定了, 每次只要传入一个x就行了


# lambda写法
def a_line(a, b):
    return lambda x: a*x+b  # lambda 前面是传入的值, 后面是表达式


line1 = a_line(5, 3)
print(line1(1))

"""
①使用闭包, 从原来传递变量的方式, 转变为传递函数的方式
②代码也要优雅很多
"""
