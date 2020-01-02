# 使用break跳出循环,程序终止, 后面的不再输出

list = [1, 3, 2, 5, 6]

i = 0
while i < len(list):
    if list[i] == 5:
        break
    else:
        print(list[i], end=' ')
    i += 1

print('')
print('**' * 10)

# 不输出 5
# continue 是跳出当前循环, 但是整个循环并没有终止
i = 0
while i < len(list):
    if list[i] == 5:
        i += 1
        continue
    else:
        print(list[i], end=' ')
    i += 1

# if 可以跟在 while 后面, 但是只有循环结束才会执行else

