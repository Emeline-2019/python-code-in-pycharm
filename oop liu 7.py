#Minxin 的案例
class Person():
    name = "Liuxing"
    age = 18
    def eat(self):
        print("eating...")
    def drink(self):
        print("drinking...")
    def sleep(self):
        print("sleeping")
class Teacher(Person):
    def work(self):
        print("working...")
class Student():
    def study(self):
        print("studying...")
class Tutor(Teacher,Student):
    pass
t = Tutor()
print(Tutor.__mro__)  # 助教这个子类mro排序列表
print(t.__dict__)   # t 这个实例的所有对象的查看
print(Tutor.__dict__)  # 查看Tutor这个子类的所有对象

print("$"*50)

class TeacherMixin():
    def work(self):
        print("working...")
class StudentMixin():
    def study(self):
        print("studying...")
class TutorMixin(Person,TeacherMixin,StudentMixin):
    pass
t = Tutor()
print(TutorMixin.__mro__)  # 助教这个子类mro排序列表
print(t.__dict__)   # t 这个实例的所有对象的查看
print(TutorMixin.__dict__)  # 查看Tutor这个子类的所有对象