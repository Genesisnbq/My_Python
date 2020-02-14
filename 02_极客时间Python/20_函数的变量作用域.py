
# ! 函数内外部变量刚好是同名的, 就会出现问题

var1 = 123


def func():
    var1 = 456  # ! 虽然函数外面也有一个 var1 但是函数里面的变量 只在函数内部起作用
    print(var1)


func()
print(var1)


# ! 可以在前面加入一个 global  就是一个全局变量了

def function():
    global var1
    var1 = 999
    print(var1)

function()
print(var1)