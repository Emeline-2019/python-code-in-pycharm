import random
secret = random.randint(1,100)  #计算机生成一个随机数
times = 3
while times :
    n = int(input("请输入数字："))
    if n == secret:
        print("你答对了！")
        break
    elif n >= secret:
        print("你的数字太大了！")
        times = times - 1
    else:
        print("你输入的数字太小了")
        times = times - 1
print("你的次数用完了！")


