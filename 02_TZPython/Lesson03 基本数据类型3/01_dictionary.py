#!/usr/bin/env python		# 指定Python解释器的路径，这个在linux类的操作系统才有意义
# -*- coding: utf-8 -*-		# 指定当前文件字符编码格式为“utf-8”
# author:Genesis_Nbq time:19/11/25 18:29DATE} 18:29

D = {
    'k1': 'v1',
    'k2': 'v2',
    'k3': 'v3',
}

print(D.items())
print(D.keys())
print(D.values())

# 通过 key 取  value 值
print(D['k1'])

#  通过 get  返回 value 值
print(D.get('k3'))
print(D.get('k4', '没有这个值'))  # 可以自定义返回值
print(D)
print('*' * 20)
# 第三种  setdefault  如果没有就会增加一个key值
print(D.setdefault('k3'))
# D.setdefault('key',d)
print(D.setdefault('k4', 'v4'))  # 默认为 none 如果设置了d  就为d
print(D)

print('=' * 20)

# 修改单独字典中的值
print(D['k1'])
D['k1'] = 'w'
print(D['k1'])

# 增 key 有则改 无则增
print(D.setdefault('k5', 'v5'))
print(D)

# 删除   删除指定 key值所在的项
a = D.pop('k5')
print(a)

print(D)
print('=' * 20)
#  popitem 每次都删除最后一个项
D.popitem()
print(D)
# [] ()
b = D.popitem()
print(b)

# clear   最后打印出一个空的字典
D.clear()
print(D)
