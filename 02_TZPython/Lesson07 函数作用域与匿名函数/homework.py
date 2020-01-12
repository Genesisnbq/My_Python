
# ! 1. 上课讲的例子都敲一遍

#! 2. 定义一个函数, 能够输入字典和元组
"""
函数返回一个字典和元组, 字典的value值和元组的值交换
eg:
tu = ('nbq', 18, 180)
di = ('name': 'liuyifei','age': 20, 'height': 50)
"""

s = '(1, 5, 6 ,4)'
t = eval(s)
print(t)
print(type(t))

print('='*20)

# !  面向过程编程
l1 = ['k1', 'k2', 'k3']
l2 = ['v1', 'v2', 'v3']


# !  zip会打包为元组
print(zip(l1, l2))
print(list(zip(l1, l2)))

# ! dict 将元组转化为 字典
print(dict(zip(l1, l2)))


tu = ('刘亦菲', 20, 40)
d1 = {'name': 'nbq', 'age': 19, 'height': 50}


print(dict(zip(d1.keys(), tu)))


def change(di, tu):
    print(dict(zip(d1.keys(), tu)))


a = {'name': 'nbq', 'age': 19, 'height': 50}
b = ('鞠婧祎', 20, 40)
change(a, b)

# ! 面向过程, 把功能封装成函数
print('='*20)


def new(di, tu):
    return dict(zip(di.keys(), tu)), tuple(di.values())


x, y = new(a, b)
print(x)
print(y)
