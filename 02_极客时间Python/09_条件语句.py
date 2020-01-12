x = 'abcd'
if x == 'abc':
    print('x的值与abc相等')
else:
    print('x与abc不相等')


# ! 条件语句: if
"""
elif == else if


            关键字                               
if 语句:    判断条件表达式
            判断为真时的代码块

    if 表达式: 
        代码块
"""

chinese_zodiac = '鼠牛虎兔龙蛇马羊猴鸡狗猪'
year = int(input('请用户输入出生年份: '))

if chinese_zodiac[year%12] =='龙':
    print ('龙年运势非常好')

    
