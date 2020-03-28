import datetime
import time

print(time.time())  # 从1970年1月1日到现在经历的秒数

print(time.localtime())  # 当前时间

print(time.strftime('%Y-%m-%d : %H:%M:%S'))  # 该大写就要大写 可以自定义格式

print(time.strftime('%y%m%d'))

# 获得10分钟以后的时间
print(datetime.datetime.now())  # 年月日 时间

newtime = datetime.timedelta(minutes=10)  # 时间的  hours=...
print(datetime.datetime.now() + newtime)  # 获得现在的10分钟之后

# 获得指定日期的 10分钟之后
one_day = datetime.datetime(2008, 5, 27)
new_date = datetime.timedelta(minutes=10)  # days = ....
print(one_day + new_date)
