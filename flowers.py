for f in range(100,1000):
    temp = list(str(f))
    a = int(temp[0])  # 此处用int将str的类型进行转换
    # print(type(a))
    b = int(temp[1])
    c = int(temp[2])
    # print(a,b,c)
    if f == a ** 3 + b ** 3 + c ** 3:  # 注意求立方的表达方式
        print(f)


