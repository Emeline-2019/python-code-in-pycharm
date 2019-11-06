print(int(3.84))   #使用int将小数转换成整数，结果是向下取整

year = input("请输入一个年份：")
if year.isdigit():
    year = int (year)
    if year % 4 == 0 and year % 100 != 0:
        print(str(year) + "闰年")    #这里的str是把原来的int类型转换，相同类型才能相加
    else:
        print(str(year) + "非闰年")
else:
    print ("请重新输入")