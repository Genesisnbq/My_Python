import re

phone = "123-456-789 # 这是注释"
p = re.sub(r"#.*$", '', phone)
print(p)

print(re.sub(r"\D", '', phone))  # 保留数字, \D 除了数字之外的字符(abc...)

string1 = 'xxx148.560.7aaaanbbb996'
pattern = re.compile(r'\D+')  # r声明这个字符里面有正则表达式  \D 数字
# +前面的字符出现一次或多次
print(re.findall(pattern, string1))
