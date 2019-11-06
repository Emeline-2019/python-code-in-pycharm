# 类的常用魔术方法
'''
- 操作类，如
    - 构造函数（__init__）,
    - 对象实例化(__new__)，此函数比较特殊，一般不需要使用
    - 对象当函数使用的时候（__call__）
    - 对象当字符串使用的时候（__str__）
    - 返回字符串（__repr__）,注意与上面的区别
- 描述符相关：
    - __set__
    - __get__
    - __delete__
- 属性操作相关
    - __getattr__:访问一个不存在的属性时触发
    - __setattr__:对成员属性进行设置时触发
               - 参数：
                   - self：用来获取当前对象
                   - 被设置的属性名称：以字符串形式出现
                   - 需要对属性名称设置的值
                - 作用：属性设置时进行验证或者修改
                - 注意：在该方法中不能对属性直接进行赋值操作，否则进入死循环
- 运算分类相关魔术方法
    - __gt__:进行大于判断的时候触发的函数
                - 参数：
                     - self
                     - 第二个参数是第二个对象
                     - 返回值可以是任意值，推荐返回布尔值

'''

#__init__举例
class A():
    def __init__(self):
        print("我被调用了")
    def __call__(self):
        print("我又一次被调用了")
    def __str__(self):
        return "图灵学院的案例"
a = A()
# __call__举例
a()
# __str__举例
print(a)


#__getattr__举例
class B():
    name = "noname"
    age = 18
    def __getattr__(self, name):
        print("没找到呀")
        print(name)
b = B()
print(b.name)
print(b.addr)



# 三种方法的案例
class Person:
    # 实例方法
    def eat(self):
        print(self)
        print("eating...")
    # 类方法
    # 类方法的第一个参数，一般命名为cls,区别于self
    @classmethod
    def play(cls):
        print(cls)
        print("playing...")
    # 静态方法
    # 没有参数，不需要用第一个参数表示自身或类
    @staticmethod
    def say():
        print("saying...")
yueyue = Person()
# 实例方法
yueyue.eat()
# 类方法
Person.play()
yueyue.play()
# 静态方法
Person.say()
yueyue.say()