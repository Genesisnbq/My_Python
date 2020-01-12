
"""
while 语句:
    while 表达式:
        代码块

for 语句:(基本用来遍历)
    for 迭代变量 in 可迭代对象: 
        代码块
"""


chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

for cz in chinese_zodiac:
    print(cz)

for i in range(0, 12):
    print(chinese_zodiac[i], end=' ')

print('')

for year in range(2000, 2021):  # ! 2000-2020年的生肖
    print('%s 年的生肖是 %s' % (year, chinese_zodiac[year % 12]))


#! while循环
"""
一直运行的时候, 可以 while True:
                        print('a')
                        if XXX:
                            break
"""

num = 5
while True:
    print('a')
    num += 1
    if num > 10:
        break
