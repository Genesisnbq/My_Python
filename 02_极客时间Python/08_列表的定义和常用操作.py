
# ! 列表和元组的区别在于列表可以增加和删除元素
a_list = ['abc', 'xyz']
a_list.append('X')

print(a_list)

a_list.remove('xyz')
print(a_list)


# ! 列表也属于序列, 所以都有:
"""
成员关系操作符: in、 not in-----> 对象 [not] in 序列
连接操作符: +   ----------------> 序列+序列
重复操作符: *   ----------------> 序列 * 整数
切片操作符: [:] ----------------> 序列 [0:整数]
"""
