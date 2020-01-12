li = [1, 3, 5, 7, 9]
for i in li:
    print(True if i > 5 else False, end=' ')
print("")

print('='*20)

#! 函数


def sum(a, b):
    res = a + b
    return res


c = 1
b = 2
print(sum(b, c))

#! 函数命名不能以数字和下划线开头


def f(list):
    for i in list:
        print(True if i > 5 else False, end=' ')
    print("")


a = [1, 3, 5, 7, 9]
f(a)
