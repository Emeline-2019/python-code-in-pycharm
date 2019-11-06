# 随机数模块
import random
# random() 获取0-1之间的随机小数，包含0，不包含1
# randint() 随机指定开始和结束之间的整数值
# randrange() 获取指定开始和结束之间的整数值，可以指定间隔值
for i in range(10):
    print(random.random())
    print(random.randint(1,9))
    print(random.randrange(1,9,3))

# choice() 随机获取列表中的值
print(random.choice([345,534,56]))
# shuffle() 随机打乱秩序列，返回值是None
list1 = [675,332,658,854]
print(list1)
print(random.shuffle(list1))
print(list1)
# uniform() 随机获取指定范围内的值（包括小数）
for i in range(10):
    print(random.uniform(1,9))