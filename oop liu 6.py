# mro的用法
class A():
    pass
class B(A):
    pass
print(A.__mro__)  #用来解析该类的全部家族关系，第一个是本身，第二个是A的父类（object）
print(B.__mro__)


# 构造函数 案例1
class A():
    def __init__(self):
        print("A")
class B(A):
    def __init__(self,name):
        print("B")
        print(name)
class C(B):
    pass
# 此时先查找C的构造函数，如果没有，则向上查找，这里找到了B的构造函数
m = C("我是名字")


print("&"*50)

# 构造函数 案例2 调用顺序
class A():
    def __init__(self):
        print("A")
class B(A):
    def __init__(self,name):
        print("B")
        print(name)
class C(B):
    # C想扩展B的构造函数，即：调用B的构造函数后还想添加一些功能
    # 两个方法
    '''
    #第一种是通过父类名调用
    def __init__(self,name):
        #首先调用父类的构造函数
        B.__init__(self,name)
        #其次增加自己的功能
        print("这是C的添加功能")
    '''
    # 第二种，使用super调用
    def __init__(self,name):
        #首先调用父类构造函数
         super(C,self).__init__(name)
        #其次增加自己的功能
         print("这是c的添加功能")
# 此时先查找C的构造函数，如果没有，则向上查找，这里找到了B的构造函数
m = C("我是名字")