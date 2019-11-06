# 类相关函数
# issubclass
class A():
    pass
class B(A):
    pass
class C():
    pass
print(issubclass(B,A))
print(issubclass(C,A))
print(issubclass(B,object))

print("$"*50)

# isinstance
class A():
    pass
a = A()
print(isinstance(a,A))

print("$"*50)

# hasattr
class A():
    name = "noname"
a = A()
print(hasattr(a,"name"))
print(hasattr(a,"age"))