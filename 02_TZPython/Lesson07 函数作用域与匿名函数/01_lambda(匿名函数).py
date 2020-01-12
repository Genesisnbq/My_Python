
# ? 简单函数


def f1():
    return 123


res = f1()  # ? 函数调用
print(res)

print("*"*20)

# ! lambda


f2 = lambda: 12345


res = f2()

print(res)

print("="*20)
# ? sum


def sum(a, b):
    return a+b


res = sum(1, 3)
print(res)

print("="*20)

f3 = lambda a,b:a+b    #* 前面是 参数:返回值
print(f3(9,9))

print('='*20)

#! filter (func,list)0 把li中 每一个元素都在  func中跑一遍  然后把符合func条件的留下

li = [1, 3, 5, 5, 67, 55, 54, 3]

def f1(x):
    return x>5
print(list(filter(f1,li)))

print('*'*20)

f1 = lambda a:a>5

print(list(filter(f1,li)))

print("="*20)

#! 实现匿名函数的输入
#! eval() 执行字符串
func = input("请输入一个匿名函数:") #* 拿到的是字符串
# print(func)
func= eval(func)

def test(a,b,function):
    return function(a,b)

num = test(11,22,func)

print(num)

print('='*20)


#  * 实现输入函数循环执行

while True:
    func = input("请输入一个匿名函数:") #* 拿到的是字符串
    func= eval(func)
    num = test(11,22,func)
    print(num)
    print('='*20)
    flag  = input('继续? y/n: ')
    if flag.lower()=='y': continue
    else : 
        print('程序结束!')
        break

