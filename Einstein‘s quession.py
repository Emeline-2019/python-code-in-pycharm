
a = 0
while a < 10000:
    if a % 2 == 1 \  # 反斜杠表示同一个语句的换行
    and a % 3 == 2 \
    and a % 5 == 4 \
    and a % 6 == 5 \
    and a % 7 == 0:
        print(a)
        a += 1    # 等价于 a + 1 = a
    else:
        a = a + 1
print("循坏结束啦")
