
# ! 文件内建(默认自带)函数和方法
"""
open() 打开文件
read() 输入
readline() 输入一行
seek() 文件内移动
write() 输出
close() 关闭文件
"""
# ! 没有加 mode 就是只读
file1 = open('name.txt', 'w')
file1.write('诸葛亮')

# ! 保存 close
file1.close()

"""
open()--->write()--->close() 写入
open()--->read()----close() 读取
"""

file2 = open('name.txt')
print(file2.read())
file2.close()

# ! 增加
file3 = open('name.txt','a') #todo a表示增加
file3.write('\n刘备')
file3.close()
file3 = open('name.txt')
print(file3.read())
