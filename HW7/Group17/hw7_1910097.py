# 1.编写函数，接收两个正整数作为参数，返回一个元组，
# 其中第一个元素为最大公约数，第二个元素为最小公倍数。


def gcd_lcm(a, b):
    product = a * b
    while b != 0:
        c = b
        b = a % b
        a = c
    return a, int(product/a)


print(gcd_lcm(14, 18))
print("-----------")
# 2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，
# 字母，空格，以及其它的个数。

string = input("输入一句话：")


def count(s):
    letter = 0
    number = 0
    blank = 0
    other = 0
    for each in s:
        if each.encode().isalpha():
            letter += 1
        elif each.isdigit():
            number += 1
        elif each.isspace():
            blank += 1
        else:
            other +=1
    print("数字{}个,字母{}个,空格{}个,其他字符{}个".format(number, letter, blank, other))


count(string)
