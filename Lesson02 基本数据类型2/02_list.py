# 列表 list
# 列表初始化
a = []  # 空列表
print(type(a))

b = [1, True, 'abc', []]
print(type(b))

#  list的常用功能, 索引
L = ['a', 'b', 'c']
print(L[0])
print(L[::-1])

# 列表是有序的可变的元素集合
L[0] = 'w'
print(L)

s = 'abc'  # 字符串只能重新赋值, 不能直接改
# s[0] = 'w

#  list切片
L = ['a', 'b', 'c']
print(L[:2])
print(L[-3:-1])
#  包头不包尾

#  排序 sort
G = ['y', 'x', 'z']
# 正序
G.sort()
print(G)

#  逆序
G.sort(reverse=True)
print(G)

# 或者直接 .reverse
a = ['5', '4', '999']
a.reverse()
print(a)
a.sort()
print(a)

# 增删改查
a.append('8')
print(a)  # 加在最后

b = [1, 2, 3]
a.extend(b)
print(a)

# 插入  在 1 这个位置插入一个 w
a.insert(1, 'w')
print(a)

# 删除  pop 删除一个尾部元素
a.pop()
print(a)

temp = a.pop()
print(temp)
print(a)

# remove 移除指定元素  只会从左边起,第一个指定的元素
a.append('w')
print(a)
a.remove('w')
print(a)

# 可以直接从下标删除
del (a[0])
print(a)

# 包含 in  看一下这个东西在不在里面
L = ['a', 'b', 'c']
a = 'c'
b = 'd'
print(a in L)
print(b in L)


