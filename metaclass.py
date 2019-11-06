# 元类演示
# 元类写法是固定的，必须继承自type
# 元类一般命名以MetaClass 结尾
class TulingMetaClass(type):
    # 注意以下写法
     def __new__(cls, name, bases, attrs):
         # 自己的业务处理
         print("haha,我是元类呀")
         attrs['id'] = '000'
         attrs['addr'] = "北京市海淀区"
         return type.__new__(cls, name, bases, attrs)
# 元类定义完就可以使用，使用注意写法
class Teacher(object, metaclass=TulingMetaClass):
    pass
t = Teacher()
print(t.addr)
