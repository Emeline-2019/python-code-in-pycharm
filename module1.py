# 查看系统保留的关键字，不可以用来当做变量的命名
import keyword
print(keyword.kwlist)


# 数学模块
import math
# print(math)   按ctrl+/ 表示注释
# ceil() 表示向上取整操作
# floor() 表示向下取整操作
# help(math.floor)
print(math.ceil(5.07))
print(math.floor(5.07))
# round() 四舍五入操作，不是数学模块中的，是python内置函数
print(round(5.1))
print(round(5.5))
# sqrt() 开平方操作,且返回浮点数
print(math.sqrt(18))
# pow() 与幂运算类似，计算一个数的N次方，有两个参数，第一个是底数，第二个是指数返回值为浮点型
print(math.pow(3,2 ))
# 幂运算,返回值为整形
print(3**2)
# fabs() 对一个数值获取绝对值，返回值为浮点型
print(math.fabs(-1))
print(math.fabs(3))
print(math.fabs(0))
# abs() 获取绝对值，不是数学模块中的，是python内置函数，返回值由原数值本身决定
print(abs(-1))
print(abs(-2.6))
# fsum() 对整个序列求和,返回值为浮点型
print(math.fsum([1,4,3,2]))
# sum() 对整个序列求和,不是数学模块中的，是python内置函数，返回值由原数值本身决定
print(sum([1,4,3,2]))
# modf() 将一个浮点数拆分成整数部分和小数部分
print(math.modf(3.45))
print(math.modf(2))
#copysign() 将第二个数的符号（正负号）传给第一个数，返回第一个数值的浮点数
print(math.copysign(2,-3))
print(math.copysign(-6,3))

