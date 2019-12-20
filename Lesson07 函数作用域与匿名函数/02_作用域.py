
# ?函数作用域
# ! 变量作用的范围就是作用域
# * 函数内部定义的变量是局部变量
# * 函数外部定义的变量是全局变量

num = 100

def f():
    num = 200
    print("1:", num)


print("2:", num)

f()

print("3:",num)

print('='*20)

# ! global  在函数内部定义全局变量
def  f1():
    global num
    num = 200
    print("1:",num)

f1()
# * 已经被修改了
print(num)

print('='*20)

# ! nonlocal  使用外层函数的变量
def f2():
    num = 66

    def f3():
        num = 88
        num += 1
        print("1:", num)
    
    f3()
    print('2:',num)


f2()  # ! 调用

print('='*20)

def f3():
    num = 66

    def f4():
        nonlocal num
        num += 1
        print("1:", num)
    
    f4()
    print('2:',num)

f3()

# * 总结:
"""
1.  函数内部定义的为局部变量, 其作用域是局部作用域, 函数外无法调用
2.  函数外定义的为全局变量, 其作用域是全局作用域, 如果函数内想要进行修改, 需要 global
3. 外层函数的变量, 如果想要在内层函数进行修改, 就需要用到 nonlocal
"""