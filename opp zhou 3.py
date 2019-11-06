'''
定义一个列表的操作类 Listinfo
包括的方法：
1、列表元素添加: add_key()  添加的元素必须是整数或字符串
2、列表元素取值：get_key()
3、列表的合并：update_list(list)
4、删除并且返回最后一个元素：del_key()
'''
class ListInfo(object):
    def __init__(self, list_val):
        self.list = list_val
    def add_key(self, key_name):
        # 添加的key 必须是数字或字符串
        if isinstance(key_name,(str,int)):
            self.list.append(key_name)
            print(self.list)
            return "ok"
        else:
            return"请输入数字或字符串"

    def get_key(self,index):
         # 判断传入的索引是否超出了列表
         if index >= 0 and index < len(self.list):
             return self.list[index]
         else:
             return "你输入的太多了"

    def update_list(self, new_list):
        self.list.extend(new_list)
        return self.list
    def del_key(self):
        # 首先要判断列表里是否有元素
        if len(self.list) >= 0:
            return self.list.pop(-1)  # 删除最后一个元素
        return"列表是空的"
ls = ListInfo([1,3,4,5,6,3])
print(ls.add_key("adfads"))   # 验证第二个def
print(ls.get_key(98))    # 验证第三个def
print(ls.update_list([88,99,284]))  # 验证第四个def
print(ls.del_key())   # 验证第五个def