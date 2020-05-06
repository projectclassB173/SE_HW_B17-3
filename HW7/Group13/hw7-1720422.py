# 1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
import math


def Calculation(x, y):
    r = math.gcd(x, y)
    return r, (x * y) // r


print(Calculation(24, 30))


# 2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。
def num(str):
    x = y = z = m = 0
    for i in str:
        if i.isdigit():
            x += 1
        elif i.isalpha():
            y += 1
        elif i.isspace():
            z += 1
        else:
            m += 1
    print("数字{}个，字母{}个，空格{}个，其他字符{}个".format(x,y,z,m))

num(input("请输入一个字符串："))