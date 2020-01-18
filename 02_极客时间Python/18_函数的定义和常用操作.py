import re

# ! 读取人物名称
f = open('name.txt', encoding='utf-8')
data = f.read()
print(data.split('|'))
f.close()

# ! 提取兵器谱
f2 = open('weapon.txt', encoding='utf-8')
# data2 = f2.read() #!直接读取到文件的结尾了
i = 1
for line in f2.readlines():
    if i % 2 == 1:
        print(line.strip('\n'))  # ! 把我们字符串中的哪些内容进行一个精简
    i += 1
f2.close()

f3 = open('sanguo.txt', encoding='utf-8')
print(f3.read().replace('\n', ''))
f3.close()

# !大量重复的语句块, 用函数进行包装
"""
def 函数名称:   #! 函数的定义
    代码
    return 需要返回的内容

函数名称() #! 函数的调用
"""


def func(filename):
    print(open(filename, encoding='utf-8').read())


func('name.txt')


def find_item(hero):
    with open('sanguo.txt', encoding='utf-8') as f:
        data = f.read().replace('\n', '')
        count = re.findall(hero, data)  # ! hero 在 data中出现多少次在列表中就有多少个
        print('主角 %s 出现 %d 次' % (hero, len(count)))
    return len(count)


# !  读取人物的信息
name_dict = {}
with open('name.txt', encoding='utf-8') as f:
    for line in f:
        names = line.split('|')
        for n in names:
            # print(n)
            name_num = find_item(n)
            name_dict[n] = name_num

print(name_dict)

# ! 后边会有详细的排序
