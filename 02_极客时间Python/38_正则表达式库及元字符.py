
# 日常应用比较广泛的模块是：
# 1. 文字处理的 re
# 2. 日期类型的time、datetime
# 3. 数字和数学类型的math、random
# 4. 文件和目录访问的pathlib、os.path
# 5. 数据压缩和归档的tarfile
# 6. 通用操作系统的os、logging、argparse
# 7. 多线程的 threading、queue
# 8. Internet数据处理的 base64 、json、urllib
# 9. 结构化标记处理工具的 html、xml
# 10. 开发工具的unitest
# 11. 调试工具的 timeit
# 12. 软件包发布的venv
# 13. 运行服务的__main__

import re

p = re.compile('a')

print(p.match('a'))
print(p.match('b'))

s = re.compile('cat')
print(s.match('cat'))

g = re.compile('ca*t')  # 输入一个 * 就可以匹配了 不然就是None 正则表达式
print(g.match('caaaaat'))

# 元字符
p = re.compile('...')  # x个. 表示匹配 x个任意字符
print(p.match('倪彬琪'))


p = re.compile('jpg$')  # 以jpg为结尾的字符  可以匹配文件
print(p.match('aaa.jpg'))


p = re.compile('ca*t')  # *号前面字符0-n 个  注意 没有也算, 这个容易错
print(p.match('caaaat'))
print(p.match('ct'))
print(p.match('caaaat'))

# ^ 从开头进行搜索  $以什么作为结尾
p = re.compile('^a')
print(p.match(''))

p = re.compile('ca{4,6}t')  # {} 表示出现次数的一个区间
print(p.match('caaaat'))


"""
cat
cbt
cct
cft

p = re.compile('c[abcf]t') # 'c.t' 就不适用了

"""
p = re.compile('c[abcf]t')
print(p.match('cft'))


# . ^ $ * + ? {} [] | \d \D \s ()
# + 表示前面这个字符出现1-n次
# ? 表示前面这个字符出现0次或一次 (有更多的作用)
# \d 表示匹配的内容是一个数字  [0-9]+ 和 \d 的功能是一模一样的
# \D 匹配不包含数字的
# () 分组   2020-03-01  (2020)-(03)-(01).group()  使用正则分组来提取
# (03|04) 只提取03或者04 如果是. 05等等都会被提取
# ^$ 表示这一行是空行
# .*? 不使用贪婪模式 abcccccd abc*(贪婪模式)

p = re.compile('abc*')  # *号匹配的时候, 会尽可能长去匹配
print(p.match('abccccccd'))

p = re.compile('abc*?')
print(p.match('abcccccd'))
print(p.match('abd'))

# <img /img>

