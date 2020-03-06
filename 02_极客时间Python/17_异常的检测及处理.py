# ! 异常检测及处理
"""
异常时出现错误后采用正常控制流以外的动作
异常处理的一般动作: 检测到错误, 引发异常, 对异常进行捕获的操作
try:
    <监控异常>
except Exception[,reason]:
    <异常处理代码>
finally:
    <无论异常是否发生都执行>

"""

"""
NameError
SyntaxError
IndexError
KeyError  d = {'a': 1,'b':2} print(d['c']) key:value
ValueError year = int(input('请输入年份: '))  abc   应该输入数字
AttributeError: 属性错误
"""
try:
    year = int(input('请输入年份: '))
except ValueError:
    print('年份要输入数字!')

# a = 123
# a.append()
# except (ValueError,AttributeError,KeyError) #! 组合成一个元组

try:
    print(1 / 0)
except ZeroDivisionError as c:
    print('0不能做除数 %s' % c)

# todo 错误信息叫做 Exception

try:
    print(1 / 1)
except Exception as c:  # !捕获所有错误信息
    print("%s" % c)

try:
    raise NameError('hello_error')  # 手动抛出异常
except NameError:
    print('my custom error')

try:
    cur = open('name.txt')
except Exception as e:
    print(e)
finally:
    cur.close()  # ! 最终关闭文件
