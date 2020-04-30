# -*- coding: UTF-8 -*-


"""
Asahi Huang
2020.04.30

---------------------------------------------------------------------

1.编写函数，接收两个正整数作为参数，返回一个元组，
其中第一个元素为最大公约数，第二个元素为最小公倍数。

---------------------------------------------------------------------
"""


def fun1(a, b):
    x = a
    y = b
    z = x % y
    while (z != 0):
        x = y
        y = z
        z = x % y
    x = (a*b)//y
    return (y, x)


print("Please enter two number")
a = int(input("number 1:"))
b = int(input("number 2:"))
if (a < b):
    temp = a
    a = b
    b = temp
re = fun1(a, b)
print("(%d,%d) = %d" % (a, b, re[0]))
print("[%d,%d] = %d" % (a, b, re[1]))

"""
+++++++++++++++++++++++++++++++++++++++++++++
run:
$ python3.7 hw7_1910009.py

Please enter two number
number 1:48
number 2:56
(56,48) = 8
[56,48] = 336
+++++++++++++++++++++++++++++++++++++++++++++
"""


"""
---------------------------------------------------------------------

2.编写函数，接受一个字符串作为参数，
计算并打印传入字符串中数字，字母，空格，以及其它的个数。

---------------------------------------------------------------------
"""


def fun2(st):
    countN = 0  # 数字计数
    countA = 0  # 字母计数
    countS = 0  # 空格计数
    countO = 0  # 空格计数
    for ch in st:
        if ord(ch) <= 57 and ord(ch) >= 49:
            countN = countN + 1
        elif ord(ch) <= 122 and ord(ch) >= 65:
            countA = countA + 1
        elif ch == ' ':
            countS = countS + 1
        else:
            countO = countO + 1
    return (countN, countA, countS, countO)


st = input("Please enter:")
re = fun2(st)
print("There are %d number,%d alpha,%d space and %d other in your enter."
      % (re[0], re[1], re[2], re[3]))


"""
+++++++++++++++++++++++++++++++++++++++++++++
run:
$ python3.7 hw7_1910009.py

Please enter:hello world 123&&&test
There are 3 number,14 alpha,2 space and 3 other in your enter.
+++++++++++++++++++++++++++++++++++++++++++++
"""
