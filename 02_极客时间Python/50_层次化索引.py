import numpy as np
from pandas import Series

# 多层索引

data = Series(np.random.randn(10),
              index=[['a', 'b', 'a', 'b', 'b', 'c', 'c', 'd', 'd', 'e'],
                     [1, 2, 3, 4, 5, 1, 2, 4, 5, 6]])

print(data)

# 多层索引的好处是, 可以根据索引的层次, 来提取相应的数据

print('-'*40)

print(data.unstack().stack())

print('-'*40)

print(data['b'])

# Series 一维数据
# DataFrame 二维数据
