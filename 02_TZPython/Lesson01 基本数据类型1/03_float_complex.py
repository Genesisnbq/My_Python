# import 要放到文件最上方
import decimal  # 要使用高精度 就要导入我们的高精度的库

a = 0.0
print(type(a))

s = 0.1 + 0.2
print(s)  # 0.30000000000000004
print('s的数据类型是: ', type(s))

f = decimal.Decimal(3.141592645451545441)
g = decimal.Decimal(5.2645545112454151)
decimal.getcontext().prec = 20
print(f * g)

# 复数
fushu = 12.3 + 4j
print('fushu的数据类型是: ', type(fushu))

# python 也可以进行强制类型转换
# complex(a,b)
# //todo两个参数的时候, 前后都不允许是字符串,不然会报错


