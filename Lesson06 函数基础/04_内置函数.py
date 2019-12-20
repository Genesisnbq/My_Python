# 动态参数

li = dir(__build_class__)
print(li)

print('\n', '=' * 20)

li = li[li.index('__ge__'):]  # ! index返回下标,
print(li)

print('\n', '=' * 20)

for i in range(len(li)):
    print("#{}.{}()".format(i + 1, li[i]))  # todo ()就是字符 (lll￢ω￢)

print('\n', '=' * 20)

li = [2, 5, 8]
print(len(li))
print(max(li))
print(min(li))
print(sum(li))
print(sorted(li))
print(list(reversed(li)))
print(bin(10))
print(oct(10))
print(hex(10))
print(ord('a'))  # todo 查看 ASCII码
print(chr(97))  # * ascii 码 转换为字符

# ?  enumerate 返回一个可以遍历的对象
li = [1, 3, 4, 5, 6, 8]
print(list(enumerate(li)))  # todo enumerate对象返回的是一个元组 tuple
for i in enumerate(li):
    print(i)

print(dict(enumerate(li)))  # todo enumerate(li) 返回的是键值对

# ? eval 识别表达式, 并且返回值(数字字符转化为真正的数字)

b = '1+2+10'
print(b)
print(eval(b))
print(eval('10') + 10)  # * 转化为真正的数字

print('\n', '=' * 20)

# ? exec() 识别赋值语句, 没有返回值
b = 'x+y+z'
x = 1
y = 11
z = 18
print(eval(b))  # ! 执行 字符串

print('\n', '=' * 20, '\n')

s = """
z = 10
b = x + y + z
print(b)
print('ok')
"""

exec(s)
x = 10
y = 15
print('\n', '=' * 20, '\n')

exec(s, {'x': 100, 'y': 999})  # ? 传参

print('\n', '=' * 20, '\n')

exec(s, {'x': 99, 'y': 1}, {'x': 1, 'y': 88})  # todo 逗号表达式以表达式右边为主


# todo filter() 过滤器
# todo i = filter(函数, 可迭代对象)
# ? 过滤 , 每个可迭代对象去执行函数, 符合条件的留下, 不符合的删去

def test(x):
    return x > 10


print('=' * 20)

list2 = [10, 11, 2, 5, 6, 99]
print(list(filter(test, list2)))

# ? map 对数据进行处理
print('=' * 20)


def test2(x):
    return x * 10


list3 = [1, 2, 3, 4, 5]
print(list(map(test2, list3)))
print('=' * 20)
# * zip 将对象逐一的配对
list4 = ['k1', 'k2', 'k3']
list5 = ['v1', 'v2', 'v3']

print(zip(list4, list5))
print(list(zip(list4, list5)))
