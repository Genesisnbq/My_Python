import re

p = re.compile('.')
print(p.match('c'))

p = re.compile('.{3}')  # 任意一个字符出现了3次 相当于'...'
print(p.match('bat'))

p = re.compile('....-..-..')
print(p.match('2020-03-01'))

p = re.compile(r'(\d+)-(\d+)-(\d+)')  # 加一个r 就不会转义了
print(p.match('2020-03-01'))
print(p.match('2020-3-1'))
print(p.match('2020-3-14').group())  # 取出所有的部分
print(p.match('2020-3-14').group(1))  # 取出第一个括号包裹的部分

year, month, day = p.match('2020-3-14').groups()
print(year, month, day)
