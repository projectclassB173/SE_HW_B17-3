
# 题目<1>
import math


def Calculation(m, n):
    r = math.gcd(m, n)
    return r, (m * n) // r


print(Calculation(15, 21))


# 题目<2>

def Count(s1):
    a = b = c = d = 0
    for i in s1:
        if i.isdigit():
            a += 1
        elif i.isalpha():
            b += 1
        elif i.isspace():
            c += 1
        else:
            d += 1
    print("数字{}个，字母{}个，空格{}个，其他字符{}个".format(a, b, c, d))


Count(input("请输入一个字符串："))