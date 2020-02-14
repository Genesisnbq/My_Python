
fd = open('name.txt')

try:
    for line in fd:
        print(line)
finally:
    fd.close()

# 经常使用, 其实这样的写法是不优雅的
# 可以写成:

with open('name.txt') as f:  # 上下文管理器
    for line in f:
        print(line)

"""
讲完类和对象后, 会详细解释如何去编写这种上下文管理器
"""

"""
统计小说人物出现次数案例总结:
    调用函数
    创建函数
    可变长参数
    变量的作用域
    匿名函数
    生成器
    迭代器
    装饰器
    闭包
"""
