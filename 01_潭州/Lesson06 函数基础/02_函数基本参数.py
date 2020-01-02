# 形参
def sum(a, b, c):  # 形参
    res = a + b + c
    return res


sum(1, 2, 3)  # 实参 因为按照位置一一对应, 所以也叫位置参数


def add(a=111, b=999, c=666):  # xxx = xx 是默认参数
    res = a + b + c
    return res


print(add(1, 1))

add(b=10, a=100, c=1000)  # 关键字参数   给形参传值, 不需要按照为位置来

# 注意: 关键字参数和位置参数一起使用时, 关键字参数要写在位置参数的后面,这是语法
