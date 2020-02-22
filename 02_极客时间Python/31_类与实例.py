user1 = {'name': 'ton', 'hp': 100}
user2 = {'name': 'jerry', 'hp': 80}


def print_role(rolename):
    print('name is %s, hp is %s' % (rolename['name'], rolename['hp']))


print(user1)  # 面向过程编程: 根据一个程序执行的顺序来编写相应的函数(从上到下)


# 面向对象编程

class Player():  # 定义一个类
    def __init__(self, name, hp):  # 这个类里面, 事先已经预定义了一些功能
        self.name = name  # 相当于userx.name
        self.hp = hp  # 相当于userx.hp

    def print_role(self):  # 定义一个方法
        print('%s: %s' % (self.name, self.hp))


user1 = Player('ton', 100)  # 类的实例化
user2 = Player('jerry', 80)
user1.print_role()
user2.print_role()

"""
编程的规范, 所有的类都是以大写字母运行的
面向过程更符合机器, 面向对象更符合人的使用习惯
self 表示类的实例化的本身, 
__init__(会自动执行) 表示一个特殊的方法, 在类进行实例化的时候,会自动执行
"""
