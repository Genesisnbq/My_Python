# ! 每个对象所特有的叫做属性


class Cat:
    """这是一个猫类"""
    pass


Kitty = Cat()

# ! 句点法, 给实例赋值属性
Kitty.color = 'white'
Kitty.eat = 'milk'

print(Kitty)
print(Kitty.color)  # todo 找到 kitty.color 所应用的对象, 并获取color 属性值
print(Kitty.eat)


class Cat:
    """ 这是一个猫类"""
    count = 0  # ! 类属性

    def __init__(self, color, eat):
        self.color = color  # ! 实体属性, 记录具体对象的特征
        self.eat = eat
        # !  计数
        print(self.color)  # ! 内部调用
        Cat.count += 1  # todo 内部调用: 类名.类属性


print('=' * 20)

Kitty = Cat('white', 'milk')
print(Kitty.color)

john = Cat('yellow', 'beats')

print(john.color)  # todo  外部调用  实例名.属性

# ! 类属性: 记录与类相关的属性

print("现在创建了 {} 只猫".format(Cat.count))
print(Kitty.count)

# ! 类只能访问类属性
# ! 实例可以访问类属性和实例属性


# ! 私有属性
"""
1. 单下划线开头, 只告诉别人这是私有属性, 外部依然可以访问更改
2. 双下划线开头, 外部不能通过实例名(instancename), 属性名(propetyname)来访问或者更改 
"""


class Cat:
    def __init__(self, color, eat):
        self._color = color  # ! 实体属性, 记录具体对象的特征
        self.__eat = eat


Kitty = Cat('pink', 'meats')

print(Kitty._color)  # todo  君子协议
# print(Kitty.__eat)#todo 这个直接不能调用
