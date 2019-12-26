#  list 可以修改,但是  tuple不行
#  tuple 是有序的,不可变的集合
#  变量初始化
a = ()  # 空元组
b = (1, False, 'ab', [], ())  # 可以是任何类型的数据
print(type(a), type(b))

# 注意:
f = ('hello', )  # 对于 单元素的元组, 必须后面加一个逗号

#  tuple的常用功能
#  索引
T = ('a', 'b', 'c')
print(T[0])
# 取出元素下标
print(T.index('c'))   # 输出下标
print(T.count('c'))   # 输出元素个数

# 切片 -3 -2 -1
# 0 1 2 3
print(T[1:])
print(T[:3])
print(T[-2:])
print(T[-3:])

# 包含
T = ('a', 'b', 'c')
a = 'a'
b = 'b'
c = 'c'
print(a in T, b in T, c in T)




