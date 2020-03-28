import random  # 产生随机数的库    测试, 密码学等等

print(random.randint(1, 100))  # random.randint(x,y) 在x和y之间随机

a = []
# 'Z' = 122
for i in range(97, 123):
    a.append(chr(i))

for i in range(1, 27):
    print(random.choice(a), end="")  # 随机26个字母
