# 题目<1>
# 编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
def lxy(a, b):
    if a > b:
        a, b = b, a
    c = a * b
    while a != 0:
        r = b % a
        b = a
        a = r
    return (b, c // b)
print(lxy(12, 30))
# 结果
# (6, 60)

# 题目<2>
# 编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。
string =("lxy_1234 %$56")
def func(s):
    num=alpha=space=other=0
    for each in s:
        if each.encode().isalpha():
            num += 1
        elif each.isdigit():
            alpha += 1
        elif each.isspace():
            space += 1
        else:
            other +=1
    print(string,"其中，数字有{}个,字母有{}个,空格有{}个,其他字符有{}个".format(alpha, num, space, other))
func(string)
# 结果
# lxy_1234 %$56 其中，数字有6个,字母有3个,空格有1个,其他字符有3个