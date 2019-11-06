print("hello world")
t = input("请输入1-100的整数：")
if t.isdigit():          #先判断输入的t是否是数字类型
    t = int(t)          #如果t是整数
    if 1 <= t <= 100:
       print("bingo,完美")
    else:
       print("有点丑啊")
else:
    print("不符合要求，请重新输入")

