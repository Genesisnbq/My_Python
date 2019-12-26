
# todo 动态参数
# todo 调用函数时, 所有传入的多余的 位置参数都会被我们的args所接收,并生成一个元组
# todo 调用函数时, 所有传入的多余的 关键字参数都会被 kwargs接收, 生成一个字典


def f1(*args, **kwargs):  # todo *是关键字  kwargs 是变量名, 规范(约定俗称)
    return


def sum(*args):
    res = 0
    print(args)
    print(type(args))
    for i in args:
        print(i, end=' ')
        res += i
    print("")
    print(res)
    return res

# todo 实参==位置参数 sum(1, 3, 5)


sum(5, 6, 7)  # todo 打印的是一个元组(因为有多余的元素)

print('=='*20)

sum(5)  # todo 打印的都是一个元组

print('='*20)


def sum2(a, *args):
    print(args)
    print(type(args))


sum2(5, 6, 5, 6)
sum2(2)

print('='*20)

# todo keywords  接收关键字参数


def sum3(**kwargs):
    print(kwargs)
    print(type(kwargs))


sum3(a=5, b=2, c=66, d=55)

print('='*20)


def sum4(a, **kwargs):
    print(kwargs)
    print(type(kwargs))


sum4(a=15, b=14, c=14, d=132)  # todo kwargs接收多余的键值对


print('='*20)

# todo 混合使用


def f1(a, *args, **kwargs):  # * 先形参 再 args 再 kwargs 注意顺序
    print(a, type(a))
    print(args, type(args))
    print(kwargs, type(kwargs))


f1(1, 2, 3, 4, 5, 6, k1=123, k2=232, k3=333)

print('='*20)

# todo 为动态参数传入列表, 字典, 元组
# todo 列表


def f1(*args):
    print(args, type(args))


li = [11, 22, 33]

f1(li, 1314, 520)  # todo 整个列表变成了这个元组的一个元素
print(li)
print(*li)  # todo *号直接取值
print('='*20)


def f2(**kwargs):
    print(kwargs, type(kwargs))


dic = {'k1': 123, 'k2': 456}
f2(**dic)  # todo **直接解包就行了 因为要传入一个键值对,可以 dic=dic, 也可以直接解包


# todo 形参, 必须参数(必须要传入参数, 否则会报错)
# todo 实参(调用函数的时候, 所传进去的实际的参数)  实参也叫位置参数(因为要和参数一一对应)
# todo 关键字参数 (键值对)
# todo 动态参数 *args(多余参数形成元组)  **kwargs(多余参数形成字典)
