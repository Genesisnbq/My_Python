# 如果没有按顺序使用参数, 需要使用 xx=
print('abc', end='\n')  # 如果使用了后边的参数, 叫做关键字参数


def func(a, b, c):
    print('a= %s' % a)
    print('b= %s' % b)
    print('c= %s' % c)


func(1, 2, 3)
func(1, c=3, b=2)


# 可变长参数  单词前面加一个 *
def howlong(*other):
    print(len(other))


howlong(234, 456, 43432)
howlong()



