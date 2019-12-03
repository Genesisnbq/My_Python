#!/usr/bin/env python		# 指定Python解释器的路径，这个在linux类的操作系统才有意义
# -*- coding: utf-8 -*-		# 指定当前文件字符编码格式为“utf-8”
# author:Genesis_Nbq time:19/11/26 19:01DATE} 19:01

# 1.找出两个列表中  相同的元素
list1 = [1, 2, 3, 4, 5]
list2 = [2, 3, 4]
list1 = set(list1)  # 因为只有set 才能做 集合运算, 所以先强制转换为 set 然后再 &
list2 = set(list2)
print(list1 & list2)

"""# 2.新建一个字典, 用 3 种方法往字典里面插入值 用四种方法取出values, 用两种方法取出key"""

D = {}
D.setdefault('k1', 'v1')  # 1
D['k2'] = 'v2'  # 2
D.update({"Genesis": "nbq"})  # 3
print(D)
print('=' * 20)
print(D.get('Genesis'))  # 1
print(D['k1'])  # 2  直接取value
print(D.setdefault('k2'))
# 强转
print(list(D.values())[2])
print(D.items())
print(list(D.items())[2][1])

# 取key值
print(list(D.keys())[0])
print(list(D.items())[0][0])

"""""""# 3.定义我们学过的每种数据类型, 并且注明哪些是可变的,哪些是不可变的"""""""
list1 = []
dict1 = {}
tuple1 = ()
string1 = str()

"""""""""
# 数字类型不可变
# 字符串不可变
# 列表: 有序, 可变,允许重复元素
# 元组: 有序, 不可变, 允许重复
# 子弹: 无序, 可修改, key唯一, value可以重复
# 集合: 无序, 可修改, 不允许重复(特性: 去重)
"""""""""

L = ['hello', 'python', '!']
s = "".join(L)
print(s)

# print("{} {} {}", format(*L))
print("%s %s %s" % (L[0], L[1], L[2]))
print('='*20)
print("{} {} {}".format(L[0], L[1], L[2]))
print('='*20)
print("{} {} {}".format(*L))



