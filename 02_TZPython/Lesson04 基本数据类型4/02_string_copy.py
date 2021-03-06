import copy
# !/usr/bin/env python		# 指定Python解释器的路径，这个在linux类的操作系统才有意义
# -*- coding: utf-8 -*-		# 指定当前文件字符编码格式为“utf-8”
# author:Genesis_Nbq time:19/11/27 18:14DATE} 18:14

"""
赋值深浅复制
1. 字符串(数字): 在内存中是一次性创建的,不能直接修改,如需修改,需要重新创建
2. 列表等可修改的数据类型: 在内存中创建时以链表的形式进行创建
3. 字符串, 数字: 赋值、深浅拷贝都没有任何意义, 因为其用元指向同一个内存地址
4. 列表, 元组, 字典
"""
# 01 赋值
n1 = {'k1': 'genesis_nbq', 'k2': '123', 'k3': ['fly', 'sky']}
n2 = n1  # 只是创建了一个变量,  该变量指向原来的内存地址
print(n1)
print(n2)
print('=' * 20)

n1['k1'] = '倪彬琪'
print(n1)
print(n2)

# 浅复制  在内存中, 只是额外创建第一层数据
# 仅仅复制容器中元素的地址

print('*'*20)

# 浅拷贝

n3 = copy.copy(n1)
n1['k1'] = '刘亦菲'
print(n3)

print('=' * 20)

# 深拷贝 完全拷贝了一个副本, 容器中的地址都不一样  完全拷贝出一份
n4 = copy.deepcopy(n1)
n1['k1'] = '勿忘我'
print(n1)
print(n4)
