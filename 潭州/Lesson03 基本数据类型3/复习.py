#!/usr/bin/env python		# 指定Python解释器的路径，这个在linux类的操作系统才有意义
# -*- coding: utf-8 -*-		# 指定当前文件字符编码格式为“utf-8”
# author:Genesis_Nbq time:19/11/26 17:01DATE} 17:01

# list 有序, 可变, 允许重复
# tuple 有序, 不可变, 允许重复
# dict  无序, 可变, key必须是唯一的  value 随意
# set 无序, 重要的应用,-> 去重

# 数据类型的创建
# 1.int
n = 122
a = 1
b = 2
print(type(n))

# id   查看变量的内存地址
print(id(n))
# 为了优化内存, 对于 -5--127范围内值, 不同变量是共用一个地址的 只要数值相同
print('=' * 20)

print(id(n), id(a), id(b))

print('=' * 20)

# 由此可以说明, 不同变量是共用一个内存的(只要变量的 value 相同)
x = 1
y = 1
z = 1
print(id(x), id(y), id(z))

# str 创建方法
s = ""
s1 = str()
s2 = "Genesis"
s3 = str("Genesis")

# 如果初始化啥都没有, 那么输出一个空格
print(s, s1, s2, s3)

# 字符串的转义
print("hello world\nhello ts")

print("Genesis Eternal ", end="")  # print的第二个参数 end=
print("hello nbq")

print('=' * 10, "拼接", '=' * 10)
# +
s1 = 'hello'
s2 = 'world'
print(s1 + ' ' + s2)

# list
# 创建方法
li = []
li1 = list()
li2 = [1, 2, 3, 4]
li3 = ([1, 2, 3, 4])

# 强转
print('=' * 10, "强转", '=' * 10)
name = 'Eric'
namelist = list(name)
print(namelist)
nametuple = tuple(name)
print(nametuple)

# 元组中可以放 字典
print("=" * 10, "元组中可以放字典", '=' * 10)

a = {}
print(type(a))
# 字典的初始化
a = dict(k1=123, k2=456, k3='v3')
print(a)

# 集合
print()

print('*'*10, '集合', '*'*10)

cur = set()
cur1 = {1, 2, 3}
test = list(cur1)
print(cur1)
print(test)

print('*'*10, '万物都可强转', '*'*10)
