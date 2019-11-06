# 属性案例
# property案例
#定义一个Person的类，具有name,age属性，对于任意输入的姓名，都要用大写方式保存，年龄内部统一用整数保存
# property(fget,fset,fdel,doc)，读取的时候调用get函数功能，赋值的时候调用set函数功能，删除的时候调用功能，说明文档
class Person():
    '''
    这是一个人，
    里面有name和age属性
    '''
    #函数的名称可以任意
    def fget(self):
        return self._name*2
    def fset(self,name):
        #所有输入的姓名以大写形式保存
         self._name = name.upper()
    def fdel(self):
        self._name = "Noname"
    name = property(fget,fset,fdel,"对name的一个操作")
a = Person()
a.name = "tuling"
print(a.name)


# 类的内置属性举例
print(Person.__dict__)
print(Person.__doc__)
print(Person.__name__)
print(Person.__base__)
