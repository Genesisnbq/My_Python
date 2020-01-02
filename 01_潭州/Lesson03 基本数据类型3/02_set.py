#!/usr/bin/env python		# 指定Python解释器的路径，这个在linux类的操作系统才有意义
# -*- coding: utf-8 -*-		# 指定当前文件字符编码格式为“utf-8”
# author:Genesis_Nbq time:19/11/26 10:10DATE} 10:10

# 集合: 一个包含唯一元素的可变和无序d的集合数据类型
# 变量初始化  同list类似, 元素可以是任何类型 但是不能是list
# dict
a = {}
print(type(a))

# set
# 快速删除重复元素
a = set()
print(type(a))

b = {'a', 1, ()}

# 添加(add, update)
SE = {1, 2, 3, 4, 5, 6, 7, 8}
print(SE)
print(type(SE))

SE.add('hello')
print(SE)
print('=' * 20)

# update 要对元素进行拆分, 作为个体传入到集合中
SE.update('welcome')
print(SE)

# 删除 remove pop discard

se = {1, 2, 3, 4, 5, 6, 7, 8}
# 如果有 就 直接删除  如果 没有 就报错
se.remove(4)
print(se)
# 没有就会报错
se.pop()
print(se)
se.pop()
print(se)
# pop队头

# discard
se = {1, 2, 3, 4, 5, 6, 7, 8}
print(se)
print('=' * 20)
se.discard(4)
print(se)
se.discard(9)  # 元素不存在就不执行任何操作

# 交集  (&)
s1 = {1, 2, 5, 8}
s2 = {2, 5, 10, 11, 15}
s3 = s1 & s2
print(s3)
print('=' * 20)

#  并集 |
s1 = {1, 2, 5, 8, 10}
s2 = {2, 5, 10, 11, 15}
s3 = s1 | s2
print(s3)
print('=' * 20)
# 差集  x - y  x中所特有的
s1 = {1, 2, 5, 8, 10}
s2 = {2, 5, 10, 11, 15}
s3 = s1 - s2
print(s3)

print('=' * 20)

# 相对差集 ^  补集   去掉两个之中公共部分后的剩下部分
s1 = {1, 2, 5, 8, 10}
s2 = {2, 5, 10, 11, 15}
s3 = s1 ^ s2
print(s3)

# 去重
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
T = (2, 4, 6, 8, 10)
s1 = set(L)  # 强制转换成一个集合
print(s1)

print("=" * 20)

L = list(T)
print(L)

s2 = set(T)
print(tuple(s2))

print('=' * 20)
# 去重  放入一个set 就相当于 去重了
p = [1, 2, 2, 2, 3, 3, 4]
s = set(p)
print(s)

