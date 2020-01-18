
list1 = [1, 2, 3]
it = iter(list1)
print(next(it))  # ! 取出 list 中的第一个元素  下一次使用就会输出第二个元素, 以此类推
print(next(it))
print(next(it))
# print(next(it)) #! exception  StopIteration  这个异常

#! range
for i in range(1, 10, 2):  # ! 步长为 2    range这个函数带的参数必须是 整数
    print(i)

#! 自己实现一个迭代器


def frange(start, stop, step):
    x = start
    while x < stop:
        yield x  # ! 类似于next  但是他在函数中会记录, 然后运行一次 就在 while 循环下面停止, 再次调用继续运行
        x += step


for i in frange(1, 10, 0.5):
    print(i)

#! yield 当我需要自己构建一个 迭代器的时候, 可以使用yield 这个关键字
