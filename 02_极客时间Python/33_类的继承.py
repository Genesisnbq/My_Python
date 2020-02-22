
"""
       继承
猫科动物 -> 猫
   父类 -> 子类
"""


class Monster():
    '定义怪物类'

    def __init__(self, hp=100):
        self.hp = hp

    def run(self):
        print('移动到某个位置')

    def whoami(self):
        print('我是%s我怕谁' % (type(self).__name__))


class Animals(Monster):
    '普通怪物'

    def __init__(self, hp=10):
        super().__init__(hp)


class Boss(Monster):
    'Boss类怪物'

    def __init__(self, hp=1000):
        super().__init__(hp)

    def whoami(self):
        super().whoami()


a1 = Monster(100)
print(a1.hp)
a1.run()  # 这是对父类的输出

# 子类会自动继承父类的属性和方法

a2 = Animals(1)
print(a2.hp)
a2.run()

"""
super 父类当中已经初始化了, 字类中就不需要初始化了
super().__init__(hp)
"""


a3 = Boss(800)
a1.whoami()
a2.whoami()
a3.whoami()

"""
子类会覆盖父类(相同的方法)
所以有很多种状态, 面向对象: 多态性
"""

"""
type(x).__name__ 输出该类的名称
"""

'''
print(type(a1), '\n', type(a2), '\n', type(a3))
print(type(a1))
print(type(a2))
print(type(a3))
'''
print(type(a1), type(a2), type(a3), sep='\n')

print(isinstance(a2, Monster))

# type 类
print(type(list))

# python3 所有得对象都继承一个叫 object(对象)类 面向对象编程
# 面向对象: 封装(拒绝外部访问) 继承(字类覆盖父类) 
# 类无法直接进行引用, 需要进行实例化 a1 = Monster(100)
 