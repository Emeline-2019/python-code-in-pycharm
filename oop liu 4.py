# 私有变量的案例
class Person():
    # name是共有对象
    name = "liupi"
    # __age 是私有成员
    __age = 18
    # 这里年龄是不能被访问的
p = Person()
print(p.name)
#print(p.__age)   # 注意报错信息“'Person' object has no attribute '__age'”

# name mangling 技术
print(Person.__dict__)   # 把私有化的全部信息展示出来发现，age这个属性已经被改成_Person__age
p._person__age = 19
print(p._person__age)



# 继承的语法
# 在python中，任何类都有一个共同的父类，叫object
class Person():
    name = "NoName"
    age = 0
    __score = 100 # 考试成绩是密码，只要自己知道
    _petname = "sec"  # petname(小名)是保护的，子类可以用，但不能公用
    def sleep(self):
        print("sleeping.......")
# 父类写在括号内
class Teacher(Person):
    teacher_id = "8394"
    def make_test(self):
        print("好好考试")

t = Teacher()
p = Person()
print(t.name)
print(Teacher.name)
# 受保护的不能外部访问，但子类可以
print(t._petname)
# 私有变量只允许被当前类或对象中访问
#print(t.__score)    子类的对象不能访问父类的私有变量，报错
print((Person.__dict__))
print(t._Person__score)   # 为什么子类的对象t 也能访问私有变量？？？？

t.sleep()
t.make_test()
print(t.teacher_id)



print("&"*50)

# 子类和父类定义同一个名称变量，则优先使用子类本身
class Person():
    name = "NoName"
    age = 0
    def sleep(self):
        print("sleeping.......")
# 父类写在括号内
class Teacher(Person):
    teacher_id = "8394"
    name = "老师"
    def make_test(self):
        print("好好考试")

t = Teacher()
print(t.name)  # 这里的name有两个，优先使用子类的
print(t.age)

print("&"*50)

# 子类扩充父类功能的案例
# 人有工作的函数，老师也有工作的函数，但老师的工作需要讲课
class Person():
    def work(self):
        print("赚点小钱")
class Teacher(Person):
    def make_test(self):
        print("好好考试")
    def work(self):
        #扩充父类的功能只需要调用父类相应的函数
        #Person.work(self)
        # 扩充父类的另一种方法
        # super代表得到父类
        super().work()
        self.make_test()
t = Teacher()
t.work()