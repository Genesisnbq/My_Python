# 程序执行流程: 顺序执行, 选择执行, 循环执行

# 控制流程
print('-----1------')
print('-----2------')
print('-----3------')

# 选择执行
a = 5
if a > 3:
    print('a>5')
elif a == 3:
    print('a==3')
else:
    print('a<3')

age = 10

if age > 18:
    print('---0---')
    print('---1---')
    print('---2---')
    print('---3---')
    print('---4---')
    print('---5---')
print('---6---')

# 缩进代表的就是包含关系

# 拓展

a = int(input('请输入你的年龄:'))
# input输入的都是 字符串  可以强行转换
print(type(a))

b = int(input('请输入学号:'))
print(type(b))

if a < 18:
    print('少先队员')
elif 18 <= a < 40:
    print('青少年')
else:
    print('成熟人士')

# 语法糖: 三目运算 装饰器, lambda
a = 6
print(True) if a > 5 else print(False)
