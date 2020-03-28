import numpy as np

arr1 = np.array([2,3,4,5,6])  # 已经经过了numpy的封装, 效率上高于 python自带的list

print(arr1)
print(arr1.dtype) # 32位

arr2 = np.array([1.2,1.3,1.4,1.5,1.6])
print(arr2.dtype)

# 累加
print(arr1+arr2) # 两个数组的数量要相同
