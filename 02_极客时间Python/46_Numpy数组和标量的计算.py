import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])

print(arr1*10)  # 标量的计算,  一维数组

# 二维是矩阵

data = [[1, 2, 3], [4, 5, 6]]  # 列表中嵌套的形式

arr2 = np.array(data)
print(arr2)  # 将data转换为 二维数组
print(arr2.dtype)

# 定义一个全为0的矩阵
print(np.zeros(10))  # 定义了一个一维的数组, 数组中都是0

# 二维  3行5列
print(np.zeros((3, 5)))

# ones()  把值都置为1
print(np.ones((4, 5)))

# 置为空  np.empty() 三维
print(np.empty((2, 3, 4)))  # 因为是空值是不安全的, 所以填入了一些随机的值
#               2个矩阵 3行4列

