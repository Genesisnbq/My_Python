# 条件循环
a = 6
while a > 5:
    print('gogogogo', end='\n')
    a -= 1

# while条件满足的时候执行
# 打印 1 到 10
i = 1
while i <= 10:
    print(i, end=' ')
    i += 1

if i == 11:
    print('')


i = 0
list = [1, 3, 5, 7, 9, 11]

while i < len(list):
    print(list[i], end=' ')
    i += 1

if i == len(list):
    print('')


print('='*20)

i = 0;

while i < len(list):
    if list[i] > 5:
        print(list[i],end = ' ')
    else:
        print(False,end= ' ')
    i +=1
print('')
print('='*20) 

i =0
while i < len(list):
    print(list[i],end=' ') if list[i] > 5 else print(False,end = ' ')
    i +=1

print('\n','*'*20)

a = ['hello', 'python', '!']

i = 0
while i<len(a):
    print(a[i])
    i+=1

