# self 用法案例
class A():
    name = "liuying"
    age = 18
    def __init__(self):   # 构造函数
        self.name = "dana"
        self.age = 19
    def say(self):
        print(self.name)
        print(self.age)
class B():
     name  = "liuxiaona"
     age = 88

a = A()

a.say()  # 系统默认把a作为第一个参数传入函数

A.say(a)  # 这里self被啊替换

A.say(A)  # 此时，可以把A作为参数传入

A.say(B)  # 此时，传入的时类实例B，因为B 具有name 和 age 属性，所以不会报错

# 以上代码，利用鸭子模型（看起来是，用起来也是，不管实际是不是）