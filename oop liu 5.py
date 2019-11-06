# 构造函数的概念
class Dog():
    # __init__就是构造函数
    # 每次实例化的时候，第一个被自动的调用
    # 因为主要工作是进行初始化，所以得名
    def __init__(self):
        print(" I am init in dog")
#实例化的时候，括号内的参数需要跟构造函数参数匹配
a = Dog()

print("&"*50)

# 继承中的构造函数案例1
class Animal():
    pass
class PaxingAni(Animal):
    pass
class Dog(PaxingAni):
    def __init__(self):
        print(" I am init in dog")
#实例化的时候，自动调用了Dog的构造函数
kaka = Dog()


print("&"*50)

# 继承中的构造函数案例2
class Animal():
    def __init__(self):
        print("Animal")
class PaxingAni(Animal):
    def __init__(self):
        print("paxing")
class Dog(PaxingAni):
    def __init__(self):
        print(" I am init in dog")
class Cat(PaxingAni):
    pass
#实例化的时候，自动调用了Dog的构造函数
#因为找到了构造函数，则不再查找父类的构造函数
kaka = Dog()
# 此处应该自动调用构造函数，因为Cat没有构造函数，所以网上查找，父类PaxingAni有构造函数，于是停止再往上查找
cc =Cat()

print("&"*50)


# 继承中的构造函数案例3
class Animal():
    def __init__(self):
        print("Animal")
class BuruAni(Animal):
    def __init__(self,name):
        print("paxing")
class Dog(BuruAni):
    def __init__(self):
        print(" I am init in dog")
class Cat(BuruAni):
    pass
d = Dog()
#c = Cat()   # 当子类与父类的参数不一致，会报错，该如何处理？？？？?
c = Cat("miaomiao")  # 这里按照父类传了一个name参数"miaomiao"进去，就可以调用父类BuruAni的构造函数了