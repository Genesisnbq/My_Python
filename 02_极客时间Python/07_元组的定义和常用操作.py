
# !  元组   ('abc', "def")

zodiac_name = (u'魔羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
               u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'射手座')

zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
               (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

(month, day) = (2, 15)

# ! filter 过滤

a = (1, 3, 5, 7)
b = 4

filter(lambda x: x < b, a)

print(list(filter(lambda x: x < b, a)))

c = filter(lambda x: x < b, a)  # ! 现在 c 是一个 filter 的对象

print(c)

print(len(zodiac_name))

# !  目前的类型是 filter 该对象还未被操作, 所以要强制转换为某个类型
zodiac_day = filter((lambda x: x <= (month, day), zodiac_days))

zodiac_len = len(list(zodiac_day))

print(zodiac_len)
