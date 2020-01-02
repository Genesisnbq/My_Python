
#  ! 序列代表有序排列
#  ! 字符串、 列表、 元组都代表序列
#  ! 并且可以通过下标偏移量访问到它的一个或几个成员

# todo chinese zodiac
# todo 记录生肖, 根据年份来判断生肖

# ? 当字符串种包含了单引号, 我们就要改成双引号, 比如说, "that's"
# ? python 对单引号和双引号是没有区分的

chinese_zodiac = '鼠牛虎兔龙蛇马羊猴鸡狗猪'

print(chinese_zodiac[0])

# !  切片

print(chinese_zodiac[0:4])  # ! 访问到 4前面那一个

print(chinese_zodiac[:])  # ! 也可以倒着访问
