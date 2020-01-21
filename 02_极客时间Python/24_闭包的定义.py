#! 20.1.21
#! 闭包的思想就来源于 函数的嵌套
#! 外部函数的变量被内部函数引用, 这就叫做闭包


def func():
    a = 1
    b = 2
    return a + b


#! 可以分为 内部函数 和 外部函数
#! add 函数名称或函数的引用
#! add() 函数的调用
def sum(a):
    def add(b):
        return a + b

    return add  # ! 返回内部函数的函数的函数名称


num1 = func()
num2 = sum(2)

# todo <------>
print(num2(4))  # ! 依然进行了加法

print(type(num1), type(num2))


def counter(first=0):
    cnt = [first]

    def add_one():
        cnt[0] += 1
        return cnt[0]

    return add_one


test1 = counter()
print(test1())
print(test1())  # ! 调用一次增加 1 闭包的威力

test5 = counter(5)
test10 = counter(10)
print(test5(), test5(), test5(), test5(), test5())  # ! 达到了调用一次 +1 的效果
print(test10(), test10(), test10(), test10())

"""
如果使用函数就需要多个函数, 这就是闭包的威力了
"""
