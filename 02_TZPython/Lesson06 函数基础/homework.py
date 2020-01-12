
# * 把上节课老师上课的例子敲一遍

print("OK")
print('\n', '*'*20, end='\n'*2)

# ! 定义一个函数, 可以对输入的数据进行排序,通过参数来决定是正向排序还是反向排序

num = [1, 4, 6, 6, 7, 432, 24, 2, 2, 4424324]


def sort_1(a, option):
    if option == 'positive':
        a.sort()
    if option == 'reverse':
        a.sort(reverse=True)


op = 'reverse'

sort_1(num, op)

for i in num:
    print(i, end=' ')

print('\n'*2, '='*20)


def sort2(number, option):
    if option == 'positive':
        print(sorted(number))
    if option == 'reverse':
        print(sorted(number, reverse=True))


num2 = [1, 2, 4, 5, 6423423, 6534]
op == 'reverse'
sort2(num2, op)

#! NOtes
# * a.sort()  a.reverse(只能反转) 直接改变 列表的顺序
# * sorted() 源列表顺序不变  reversed() reverse 只能反转, 不能实现逆序
