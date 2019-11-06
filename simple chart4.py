'''
打印如下图形
     *
    * *
   * * *
  * * * *
 * * * * *
'''

# 总体思路是：1、先打印一行空格，代表每一行星星之前的空格，不换行再打印星星
# 2、可以将空格打印的那部分理解成一个倒三角形
for i in range(0,5):
    for j in range(5-i):
        print(" ",end="")
    for m in range(0,i+1):  # 注意此处与下面同样位置的区别
        print("* ",end="")
        continue
    print()


print("&"*30)
'''
打印如下图形
     * * * * * 
    * * * * * 
   * * * * * 
  * * * * * 
 * * * * * 
'''

for i in range(0,5):
    for j in range(5-i):
        print(" ",end="")
    for m in range(0,5):   # 注意此处与上面同样位置的区别
        print("* ",end="")
    print()


print("&"*30)
'''
打印如下图形
     *
    * *
   *   *
  *     *
 * * * * *
'''
# 思路：1、先打印边上的倒三角形的空白； 2、接下来在不换行的情况下打印*，首先打印最后一行，然后是剩余行的收尾*，最后打印空格
for i in range(0,5):
   for j in range(5-i):
       print(" ",end="")
   for m in range(0,i+1):
        if i == 4:
            print("* ",end="")
        else:
            if m == 0 or m == i:
                print("* ",end="")
            else:
                print("  ",end="")
   print()


