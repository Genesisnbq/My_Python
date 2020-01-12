# 字符串编码
# 计算机只认识 0 和  1
# 0/1 bit
# 1 byte =8bit 计算机的最小存储单位 1位 表示 0-255
# 0/1 = 1bit
# 1byte = 8bit    # 计算机的最小存储单位 0-255的数值
#
# 字符编码的发展史00000000
# 第一个阶段：
# 考虑英文ASCII（英文字符/键盘上的所有字符）
# ASCII码用一个字节代表一个字符
#
# 第二个阶段：
# 各个国家纷纷定制了自己的字符编码
# GBK使用两个字节（2bytes）代表一个字符 2**16-1 65535
#
# 第三个阶段：
# unicode兼容万国语言 使用两个字节（2bytes）代表一个字符
#
# 第四个阶段：
# utf-8：对英文字符1byte表示，中文3bytes
# unicode 用空间换时间
# utf-8 尽可能节省带宽, 保证数据传输的稳定性
# 编码(encode) 和 解码(decode)
# 编码: 将unicode 转化位其他指定的编码
# 解码: 将原编码转化位 unicode

s = '中'  # 当程序执行时, 会以unicode保存在内存空间中

# 编码
s1 = s.encode('utf-8')  # 3个字节
s2 = s.encode('GBK')  # 2个字节
print(s)
print(s1)
print(s2)
print(type(s))
print(type(s1))
print(type(s2))

# 巩固
a = '你好Ts'
unicode_gbk = a.encode('GBK')
print(unicode_gbk)
unicode_utf8 = a.encode('utf-8')
print(unicode_utf8)

# gbk -> utf-8
gbk_utf8 = unicode_gbk.decode('GBK').encode('utf-8')
print(gbk_utf8)

# 总结
"""
1. 各个编码的相互转换都要先转换为 unicode, 通过unicode再转其他编码
2. GBK不止这一个
"""