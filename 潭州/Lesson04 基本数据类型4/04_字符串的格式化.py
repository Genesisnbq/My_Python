# %是传统方法
# format是python 特有的

# 格式化日期
year = 2019
month = 11
day = 29
print('%04d-%02d-%02d' % (year, month, day))

f = 3.141592
print('%09.2f' % (f))  # 不足 9位就用 0来补齐  包括小数点

print('%o' % 10)  # 八进制  八进制会把多余的 2甩到第二位上

print('%x' % 10)  # 十六进制

# format python 特有
test = 'name:%s, age:%d, %s' % ("倪彬琪", 18, '刘亦菲')
print(test)

print('=' * 20)

test = 'name:{}, age:{}, nick_name:{}'.format('倪彬琪', 18, '刘亦菲')
print(test)

# 可以通过下标来赋值, 即使没有第三个值
test = 'name:{0}, age:{1}, nick_name:{0}'.format('倪彬琪', 18)
print('=' * 20)
print(test)

test = 'name:{0}, age:{1}, nick_name:{0}'.format(*['倪彬琪', 18])
print('=' * 20)
test = 'name:{name}, age:{age}, nick_name:{name}'.format(**{
    'name': '倪彬琪',
    'age': 18
})
print(test)

print('=' * 20)

# 固定数据类型
test = "numbers: {:b}, {:o}, {:d}, {:x}, {:X}, {:%}".format(
    10, 10, 10, 10, 10, 10)
print(test)
test = "numbers: {num:b}, {num:o}, {num:d}, {num:x},{num:X},{num:%}".format(
    num=10)
print('=' * 20)
print(test)

print('=' * 20)

print('{:.3f}'.format(3.1415926))
