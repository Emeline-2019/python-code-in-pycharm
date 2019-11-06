'''
打印如下图形
*
**
***
****
*****
'''
for i in range(1,6):
    print("*"*i)


print("&"*30)


'''
    
打印如下图形
*
* *
*   *
*     *
* * * * *

'''
# 方法一：

for i in range(0,5):     # 注意i的取值是0-4，共5个数字   # i 的for循环是控制行的，j 的for循坏是控制列的
     for j in range(0,i+1):
         if i == 4:
             print("* ", end="")  #此处能这么打印是因为已经加了一个内循环（即：打印列）
             continue
         else:
             if j == 0 or j == i:
                 print("* ",end="")
             else:
                 print("  ",end="")
     print()        # 这里表示要换行了，注意这个位置要对其内循环


print("%"*40)

#方法二：
for i in range(0,5):
    if i == 4:
        print("* "*5)   # 注意此处与上面的写法的不同
    else:
        for j in range(0, i + 1):
            if j == 0 or j == i:
                print("* ", end="")
            else:
                print("  ", end="")
    print()




'''
打印如下倒立三角形
* * * * *
* * * *
* * *
* *
*
'''
for i in range (5):
    for j in range(5-i):   # 倒三角是随着行号的增加，列在减少，这里用 5-i 表示这种关系，i增大，5-i的值就会变小
        print("* ",end="")
    print()



print("%"*40)
'''
打印如下倒立空三角形
* * * * *
*     *
*   *
* *
*
'''
for i in range(5):
     for j in range(5-i):
         if i == 0:
             print("* ",end="")
             continue
         if j == 0 or j ==5-i-1:
             print("* ",end="")
         else:
             print("  ",end="")
     print()