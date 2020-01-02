#!/usr/bin/env python		# 指定Python解释器的路径，这个在linux类的操作系统才有意义
# -*- coding: utf-8 -*-		# 指定当前文件字符编码格式为“utf-8”
# author:Genesis_Nbq time:19/11/26 16:51DATE} 16:51

# + - * / % ** //整除
a = 25
b = 10
print("a+b=", a + b)
print("a-b=", a - b)
print('a*b=', a * b)
print('a/b=', a / b)
print('a的b次幂=', a ** b)
print('a整除b=', a // b)

# python 读入  a = input()

# 比较运算符 == != > < >= <=

# 赋值运算符 += /= -= //= **= %=

# 逻辑运算符 and or not

# 返回的其实是值,  and 都为真 返回前面    or  返回最后一个真
print(0 and a and b)
print(a or b)  # 如果 a 是假 ,就会往后看
print(a or b or 0)
print(not a)
print(not b)
