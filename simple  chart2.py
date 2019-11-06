'''
打印以下图形
* * * * *
*       *
*       *
* * * * *
'''

for i in range(0,1):
    print("* "*5)
for j in range(0,2):
    print("*       *")
for k in range(0,1):
    print("* "*5)

print("&"*20)

#方法二
for i in range(0,4):
    if i == 0 or i == 3:
        print("* "*5)
    if i == 1 or i == 2:
        for j in range(0, 5):
            if j == 0 or j == 4:
                print("* ",end="")
            else:
                print("  ",end="")
        print()

