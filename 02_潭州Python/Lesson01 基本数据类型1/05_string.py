a = 'abcd'
b = 'hello world'
c = "welcome to Ts"
d = '''good idea'''
e = """
    红豆生南国,
    生来发几枝?
    愿君多采撷,
    此物最相思。
    """

f = '''
    红豆生南国,
    生来发几枝?
    愿君多采撷,
    此物最相思。
    '''

print('a: ', a)
print('b: ', b)
print('c: ', c)
print('d: ', d)
print('e: ', e)
print('f: ', f)

print(b.capitalize())  # 首字母大写

# [] 表示可选参数
print(a.center(10, '*'))
print(a.center(10))  # 不加参数就输出的是空格

# count
print(a.count('a'))
print(a.count('a', 1))  # 从下标 1开始

