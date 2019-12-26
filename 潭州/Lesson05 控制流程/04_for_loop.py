# 一个个读取叫做遍历

list1 = [1, 3, 5, 7, 9]

for i in list1:
    print(i, end=' ')

#  元组的遍历
print('')

print('*' * 20)

tuple1 = (1, 3, 5, 7, 1414)

for i in tuple1:
    print(i, end=' ')

# 集合 set
se = {'k1', 'k2', 'k3'}

for i in se:
    print(i)

print('*' * 20)

# 字典
se = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}

for i, j in se.items():
    print(i, j, end=' ')

# 如果是可变对象, 一定不要在循环里插入东西

# 如何判断一个对象是不是可迭代的对象: 1. 直接放到for里面 2. 如果一个对象有 iter方法, 那么就是可以迭代的

# range()
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print('')
print(range(5), end='')
print('')
print(list(range(5)))
print(list(range(1, 4)))  # 类似于切片, 到end停止 不包括end
print('=' * 20)
print(list(range(0, 11, 2)))  # strat, end ,step

# 循环
for i in range(1, 21):
    if i % 5 == 0:
        print(i, end=' ')

print('')
print('=' * 20)

# break, continue, else
# break掉的话, else 是不会运行的, 所以
for i in range(1, 100):
    if i % 9 == 0:
        print(i, end=' ')
else:
    print('')
    print('Ok')
