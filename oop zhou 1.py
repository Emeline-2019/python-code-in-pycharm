'''
定义一个学生类，有下面的属性
1、姓名
2、年龄
3、成绩（语文、数学、英语）每科成绩类型为整数 类方法
4、获取学生的姓名：get_name() 返回类型：str
5、 获取学生的年级：get_age() 返回类型：int
6、 返回3门科目中最高的分数，get_scores() 返回类型：int
'''

class Student(object):
    def __init__(self, name, age, scores):   # 构造函数
        self.name = name
        self.age = age
        self.scores = scores
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_scores(self):
        return max(self.scores)
zz = Student("周周", 18 ,[80,79,96])
print(zz.get_name())
print(zz.get_age())
print(zz.get_scores())