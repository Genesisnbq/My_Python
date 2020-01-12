# 1.定义讲过的每种数据类型, 并实现相互之间的转换
# int(a) float(a)  complex(a) bool(a)
a = 1
print(bool(a))

# 2. 自定义一个字符串(eg: a = "hello world") , 用切片的方式进行逆序
# 步长
a = "hello world"
print(a[::-1])  # 逆序
print(a[-11:])

# 3. 有一个时间形式(20191124) 要求得到年月日
a = '20191124'
print(a[:4], '年', a[4:6], '月', a[6:], '日')

# 4. 用多种方法往list中 增加值
b = [1, 2, 3, 4]
a = ['a', 'b', 'c']
b.extend(a)
b.append(1)
print(b)

# 5.list ['hello], 'python', '!'] 拼接并输出  至少使用两种方法
a = ['hello', 'python', '!']
print(a[0] + ' ' + a[1] + a[2])

# python是严格缩进的



