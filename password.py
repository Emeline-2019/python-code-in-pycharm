passwords = "abc123"
times = 3
while times:
    input_words = input("请输入密码")
    if "*" in input_words:
        print("密码中不能含有*")
    elif input_words == passwords:
        print("密码正确")
        break
    else:
        print("密码错误")
        times -= 1

