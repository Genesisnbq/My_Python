s = '     Hello, Ts'
print(s[2:4])

# 反向索引
print(s[-6:-3])

# 反过来是从 -1开始索引的

print(s[0:5:1])  # 步长为 1
print(s[0:5:4])  # 步长为 3

print(s[::-1])  # 步长为 -1  证明为逆序输出
print(s[::-2])

#  移除空白 strip()    移除两端空格移除左端的空格 lstrip    右端 rstrip
print(s)
print(s.strip())
print(s.strip('s'))  # 移除两端指定字符

# 分割 split
s = 'hello,ts'
print(s.split(','))  # 通过  ',' 分割
print(s.split())  # 如果为空,会按照空格分隔  没有空格,则把真个视为一个整体

#  指定最多分割次数
#  指定分割的地方,就是他下刀的地方, 那个地方会消失
print(s.split('l', 1))  # 最多分割一次
print(s.split('l', 2))  # 第一次那个地方,是一个空字符,然后第二次的时候,回头看,一个空字符

