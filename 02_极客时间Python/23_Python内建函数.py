#20.1.21
#todo 合并和累加操作的时候, 会使用到这几个函数
from functools import reduce
#! 20.1.20
#! Python 内建函数
"""
filter() 过滤器
map()哈希表 reduce() 
zip()
"""
# help(filter)  #! 详细的介绍

a = [1, 2, 3, 4, 5, 6, 7]
b = [3, 5, 6, 6]

#! 使用 lambda 就需要强制转化成 list

newa = list(filter(lambda x: x > 5, a))
print(newa)

# help(map)

# ! map()
print(list(map(lambda x: x, a)))
print(list(map(lambda x, y: x + y, a, b)))

print(reduce(lambda x, y: x + y, [2, 3, 4], 1))  #! reduce(函数,迭代器(列表),初始值)
"""
(2+1)+3+4=10
"""

#! zip()
"""
只要有_iter 这个方法的, 都可以使用for in 这个形式
"""

#!  纵向组合
for i in zip((1, 2, 3), (4, 5, 6)):
    print(i)
"""
zip 可以对字典中的 value 和 key进行对调
"""

dicta = {'aa': 'a', 'bb': 'b'}
dictb = dict(zip(dicta.values(),dicta.keys()))  #todo 对调成功
print(dictb)
