
#! 字典, 对应关系比较明显
#! 字典包含哈希值和指向的对象
"""
{"哈希值": "对象"}
{"length": 180,"width": 80}
"""

# !字典的定义和增加值
dict1 = {}
print(type(dict1))

dict2 = {'x': 1, 'y': 2}
dict2['z'] = 3
print(dict2)

print('*' * 20)

zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
               (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))  # !  元组的嵌套

# ! u表示该字符串是一个 unicode 对象
zodiac_name = (u'魔羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
               u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'射手座')

chinese_zodiac = '鼠牛虎兔龙蛇马羊猴鸡狗猪'

cz_num = {}
for i in chinese_zodiac:
    cz_num[i] = 0

z_num = {}
for i in zodiac_name:
    z_num[i] = 0
# ! 不够优雅


while True:
    year = int(input('请输入年份: '))
    month = int(input('请输入月份: '))
    day = int(input('请输入日期: '))

    n = 0

    while zodiac_days[n] < (month, day):
        if month == 12 and day > 23:
            break
        n += 1

    print(zodiac_name[n])
    print('%s 年的生肖是 %s' % (year, chinese_zodiac[year % 12]))

    cz_num[chinese_zodiac[year % 12]] += 1
    z_num[zodiac_name[n]] += 1

   # ! 输出生肖和星座的统计信息
    for each_key in cz_num.keys():
        print('生肖 %s 有 %d 个' % (each_key, cz_num[each_key]))

    for each_key in z_num.keys():
        print('星座 %s 有 %d 个' % (each_key, z_num[each_key]))
