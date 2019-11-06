for red in range(0,4):
    # print(type(red))   red是数值型
    for yellow in range(0,4):
        for green in range(2,7):   # 因为要抓出8个球，红色和黄色总共只有6个，所以绿色最起码要2个
            if red + yellow + green == 8:
                print("red:{}".format(red))
                print("yellow:{}".format(yellow))
                print("green:{}".format(green))
                print("$"*30)