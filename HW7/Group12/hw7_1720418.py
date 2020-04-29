# 1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
import math


def num(m,n):
    j = math.gcd(m, n)
    return j,(m * n) // j


print (num(50,30))


# 2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。

def count(n):
    numb = let = spa = cha = 0
    for i in n:
        if i.isdigit():
            numb += 1
        elif i.isalpha():
            let += 1
        elif i.isspace():
            spa += 1
        else:
            cha += 1
    print("数字{}个，字母{}个，空格{}个，其他字符{}个".format(numb, let, spa, cha))


count(input("请输入："))