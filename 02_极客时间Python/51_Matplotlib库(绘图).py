import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')  # 忽略警告

# 使用pyplot这个模块

plt.plot([1, 3, 5], [4, 8, 10])
plt.show()

x = np.linspace(-np.pi, np.pi, 100)  # x的定义域为 -3.14-3.14 中间间隔100个元素
plt.plot(x, np.sin(x))

plt.show()

# 绘制多条曲线
x = np.linspace(-np.pi*2, np.pi*2, 100)
for i in range(1, 5):
    plt.plot(x, np.sin(x/i))
plt.show()

plt.figure(1, dpi=50)  # 创建图表1, dpi代表图片精细度 dpi越大, 文件越大, 杂志要300以上

data = [1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 5, 6, 4, 4, 4, 4]  # 根据数字的数量来创建直方图
plt.hist(data)
plt.show()


x = np.arange(1, 10)
y = x
fig = plt.figure()
# c='r' 表示散点的颜色为红色, marker表示指定散点形状为圆形
plt.scatter(x, y, c='yellow', marker='o')
plt.show()

iris = pd.read_csv("iris_training.csv")
print(iris.head())

# 绘制散点图
iris.plot(kind="scatter", x="120", y="4")

plt.show()

iris = pd.read_csv("iris_training.csv")
# 设置样式
sns.set(style='white', color_codes=True)
# 设置绘制格式为散点图
sns.jointplot(x='120', y='4', data=iris, size=5)

# distplot绘制曲线
sns.distplot(iris['120'])

plt.show()

iris = pd.read_csv("iris_training.csv")
sns.FacetGrid(iris, hue="virginica", size=5).map(
    plt.scatter, '120', '4').add_legend()
sns.FacetGrid(iris, hue='virginica', size=5).map(
    plt.scatter, 'setosa', 'versicolor').add_legend()

plt.show()
