# 变量的三种用法

class A():
    def __init__(self):
        self.name = "haha"
        self.age = 18
a = A()
# 属性的三种用法
# 1、读取 ；
print(a.name)

# 2、赋值；
a.name = "liudana"
print(a.name)

# 3、删除
del a.name


print("$"*50)

# 类属性 property
# 应用场景：对变量除了上述普通的三种操作，还想增加一些附加的操作，可以通过property完成
class A():
    def __init__(self):
        self.name = "haha"
        self.age = 18
    # 此功能是对变量进行读取操作时应该执行的的函数功能
    def fget(self):
        print("我被读取了")
        return self.name
    # 对变量进行写操作的时候执行的功能
    def fset(self,name):
        print("我被写入了，但还可以做好多事")
        self.name = "tuling" + name
    # 删除变量的时候进行的操作
    def fdel(self):
        pass
    # property 的四个参数顺序是固定的
    # 第一个参数代表读取的时候需要调用的函数
    # 第二个参数代表写入的时候需要调用的函数
    # 第三个是删除
    name2 = property(fget, fset, fdel, "这是一个property的例子")
a = A()
print(a.name)
print(a.name2)
print("$"*50)
a.name2 = "xiaobai"
print(a.name2)


