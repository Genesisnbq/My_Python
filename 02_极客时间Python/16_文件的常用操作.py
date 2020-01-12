
# # ! 文件内建(默认自带)函数和方法
# """
# open() 打开文件
# read() 输入
# readline() 输入一行
# seek() 文件内移动
# write() 输出
# close() 关闭文件
# """
# # ! 没有加 mode 就是只读
# file1 = open('name.txt', 'w')
# file1.write('诸葛亮')

# # ! 保存 close
# file1.close()

# """
# open()--->write()--->close() 写入
# open()--->read()----close() 读取
# """

# file2 = open('name.txt')
# print(file2.read())
# file2.close()

# # ! 增加
# file3 = open('name.txt', 'a')  # todo a表示增加
# file3.write('\n刘备')
# file3.close()
# file3 = open('name.txt')
# print(file3.read())

# file4 = open('name.txt')
# print(file4.readline())

# file5 = open('name.txt')
# for line in file5.readlines():
#     print(line)
#     print('======')
"""
file6 = open('name.txt')
file6.read() # ! 读取文件中所有字符
"""

file6 = open('name.txt')  # ! 最开始的位置在文件的开头(称为文件的指针)
print('当前文件指针的位置: %d' % file6.tell())
print('当前读取到了一个字符, 字符的内容是: %s' % file6.read(1))
print('当前文件指针的位置: %d' % file6.tell())

#! 第一个参数代表的是偏移的位置(偏移量), 第二个参数0表示从文件的开头进行偏移,1表示从当前位置进行
#! 2表示从文件的结尾的位置开始偏移
file6.seek(5, 0)  # !从开头开始, 然后偏移 5 个位置
print('进行了seek(0)之后')
print('当前文件指针的位置: %d' % file6.tell())
print('当前读取到了一个字符, 字符的内容是: %s' % file6.read(1))
print('当前文件指针的位置: %d' % file6.tell())

file6.close()
