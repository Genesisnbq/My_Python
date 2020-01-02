
# !  判断是否在 序列内
# ! in      not in

chinese_zodiac = '鼠牛虎兔龙蛇马羊猴鸡狗猪'

print('狗' in chinese_zodiac)
print('狗' not in chinese_zodiac)

# ! 序列及基本操作

"""
成员关系操作符: in、 not in-----> 对象 [not] in 序列
连接操作符: +   ----------------> 序列+序列
重复操作符: *   ----------------> 序列 * 整数
切片操作符: [:] ----------------> 序列 [0:整数]
"""

print(chinese_zodiac + chinese_zodiac)

print(chinese_zodiac + 'abcd')

print(chinese_zodiac * 3)

