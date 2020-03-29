from pandas import DataFrame
from pandas import Series
from numpy import nan as NA  # 删除缺失值
import pandas as pd  # 多维表格

data = {"city": ['shanghai', 'zhejiang', 'jiaxing', 'sichuan', 'wuhan'],
        'year': [1, 2, 3, 4, 5],
        'pop': [23, 321312, 312312, 312312, 43]}

frame = pd.DataFrame(data)

print(frame)

frame2 = pd.DataFrame(data, columns=['year', 'city', 'pop'])  # 按这个顺序排序

print(frame2)


print('-'*40)
data = DataFrame([[1, 2, 3], [1, NA, NA], [NA, NA, NA]])
print(data)
print(data.dropna())  # 有缺失值的行直接删除
print('-'*40)
print(data.dropna(how='all'))  # 删除全部是缺失值的行
data[3] = [NA, NA, NA]
print('-'*40)
print(data)
print('-'*40)
print(data.dropna(axis=1, how='all'))  # 删除全部是na的列


print(data.fillna(0))  # 将是na的地方赋成 0

# 上面那样只是改变了副本, 如果需要自身改变, 可以增加一个参数, fillna(0,inplace=True)
print('-'*40)
print(data)
print('-'*40)
data.fillna(0, inplace=True)  # 本身修改
print(data)
