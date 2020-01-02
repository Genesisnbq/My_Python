# 字典 {}
# {key:value}
#  初始化变量
a = {}
print(type(a))

# 一般情况下, 字典的key一般使用 数字 或者 字符串, 也可以使用元组
# value 可以是任意的类型
#  并且可以进行嵌套
b = {
    1: 2,
    'k1': 'v1',
    False: True,
    'k2': [1, 2, 3],
    (1, 2, 3): (1, 2, 3),
    'k3':
        {
            1: 'a',
            2: 'b',
            3: 'c',
            4: 'd'
        }
}

# 常用功能
D = {
    'k1': 'v1',
    'k2': 'v2',
    'k3': 'v3',
    'k4': 'v4'
}
# 实现list 变成 字典
D1 = {}
L = ['a', 'b', 'c']
# 以序列 L 里的值作为 字典的 key     : value
#  fromkeys(*args, **value)
#  value 为字典所对应的初始值('v')
print(D1.fromkeys(L))
print(D1.fromkeys(L, '1'))

# 长度  len()
print(len(D))
print(D.items())  # 键值对  key对
print(D.keys())
print(D.values())

