
# ! 从1到 10 所有偶数的平方

alist = []
for i in range(1, 11):
    if(i % 2 == 0):
        alist.append(i*i)
print(alist)

# todo 不够优雅

# ! 简化
blist = [i*i for i in range(1, 11) if(i % 2 == 0)]
print(blist)

""""""

zodiac_name = (u'魔羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
               u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'射手座')
z_num = {}
for i in zodiac_name:
    z_num[i] = 0

#! python独有的语法
z_num = {i: 0 for i in zodiac_name}
print(z_num)
