'''
打印以下图形
* * * * *
* * * * *
* * * * *
'''
# 一个for循环
for i in range(0,3):
    print("* * * * *")

print("&"*20)

# 两个for循环
# 思路： i--打印行   j-- 打印列
for i in range(0,3):   #  这个for循坏负责对下面这个循坏打印次数
    for j in range(0,5):   # 这个for循坏是负责每次打印一个*
        print("*", end="")  # end="" 表示此处不换行,因为print打印默认是会换行的
    print()    # 这里表示换行