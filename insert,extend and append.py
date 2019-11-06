member = ["图灵","学院","学什么？"]
member.insert(1,"tuling")
print(member)
member.insert(3,"xueyuan")
print(member)
member.insert(5,"xueshenme?")
print(member)

ls = [1,[1,2,["tuling"]],3,4,5]
# 把“tuling"替换成10
ls[1][2][0] = "10"   # ls由三个列表组成，tuling这个成员是在第一个列表的第1位，第二个列表的第2位，第三个列表的第0位
print(ls)

ls = [(x,y) for x in range (10) for y in range(10) if x % 2 == 0 if y % 2 != 0]
print(ls)

# 复原如上列表推导公式
ls = []
for x in range(10):
    for y in range(10):
        if x % 2 == 0 and y % 2 != 0:
            ls.append((x,y))  # 把x,y 作为元组放入列表的方法，注意括号和append的用法
print(ls)