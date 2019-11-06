'''
定义一个字典类：DictClass,完成如下功能
1、删除某个key  del_dict(key)
2、判断某个键是否在字典里，如果在返回键对应的值，不在则返回“notfound"  get_dict()
3、返回键组成的列表，返回类型：list  get_key()
4、合并字典，并且返回合并后字典的values组成的列表，返回类型list update_dict()
'''

class DictClass(object):
    def __init__(self,dict):
        self.dict = dict
    def del_dict(self,key):
        # 判断key是否在字典里？
        if key not in self.dict.keys():
            #print("key 不在字典里")  # 这里把return换成print执行后多返回了一个None，为什么？？？？？-----print只是打印了内容，函数没有返回值，所以是None
            return "key 不在字典里"
        else:
            self.dict.pop(key)
            print(self.dict)      #  为什么这个print写在return后面就不会被执行？？？------函数执行到return就结束了，后面内容不会被执行
            return "删除成功"

    def get_dict(self,key):
        if key not in self.dict.keys():
            return"not found"
        else:
            return self.dict[key]
    def get_key(self):
        return self.dict.keys()
    def update_dict(self, dict2):
        self.dict = dict(self.dict, **dict2)
        return self.dict.values()

d = DictClass({"a":1,"F":2,"r":3})
print(d.del_dict("m"))   #验证第二个def
print(d.get_dict("a"))   # 验证第三个def
print(d.get_key())       # 验证第三个def
print(d.update_dict({"m":4}))  # 验证第四个def