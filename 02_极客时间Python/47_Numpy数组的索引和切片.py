import numpy as np

print(np.arange(10))  # 0-9

a = np.arange(10)
print(a[5])  # 输入第5个元素

# 可以对切片重新赋值
# 下标下标 0-9的数
print(a[0:10])

# 可以给切片赋值
a[0:10] = 1
print(a)

b = np.arange(10)
print(b)
arr_slice = b[5:8].copy()  # 下标5-7的数
print(arr_slice)

arr_slice[:] = 15
print(arr_slice)
