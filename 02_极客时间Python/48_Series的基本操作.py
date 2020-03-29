import pandas as pd 
# 将 字典转化为 Series

sdata = {'beijing':123, 'shanghai':342,'zhejiang':111}

obj2 = pd.Series(sdata)
print(obj2)

obj2.index = ["a","b","c"]  # 更改索引
print(obj2)