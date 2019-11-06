class Teacher():
    name = "dana"
    age = 19
    def say(self):
        self.name = "yaona"
        self.age = 17
        print("my name is {0}".format(self.name))
        print("my age is {0}".format(self.age))
        #调用类的成员变量需要用 __class__
        print("my age is {0}".format(__class__.age))   # 说明self不是一个关键字，只是一个参数
    def sayAgain():
        print("hello, world !")
        print(__class__.name)
        print(__class__.age)
t = Teacher()
t.say()
# 调用绑定类函数使用类名
Teacher.sayAgain()
