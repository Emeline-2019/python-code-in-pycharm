'''
定义一个学生类，用来形容学生
'''
# 定义一个空的类
class Student():
    # 一个空类，pass代表直接跳过，占坑
    # 此处pass必须有
    pass
# 定义一个对象
xiaoming = Student

# 定义一个类，用来描述学python的学生
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = "python"
    #1、注意def 的缩进
    #2、系统默认有一个self的参数
    def dohomework(self):
        print("我在写作业")
        return None
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
print(yueyue.course)
yueyue.dohomework()