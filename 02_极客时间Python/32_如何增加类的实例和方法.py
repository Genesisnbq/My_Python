class Player():  # 定义一个类
    def __init__(self, name, hp, occu):  # 这个类里面, 事先已经预定义了一些功能
        self.__name = name  # 相当于userx.name
        self.hp = hp  # 相当于userx.hp
        self.occu = occu  # 职业

    def print_role(self):  # 定义一个方法
        print('%s: %s %s' % (self.__name, self.hp, self.occu))

    def updatename(self,newname):  # 类里面的函数, 第一个参数一定要用self
        self.__name = newname 


class Monster():
    '定义怪物类'
    pass  # 我们定义了一个Monster类, 但是现在还不想去实现他


""" 
在面向对象中,变量被称为属性,函数就称为方法
"""

user1 = Player('jerry', '100', 'war')
user1.updatename('wilson') 
user1.print_role()

"""
self.__name = name
加两个下划线就不会被我们的实例访问到了(user1.name = xxx 就不行了)
__加两个下划线就是[类的封装]
"""

