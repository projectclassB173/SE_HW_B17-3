# 1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。


def process(m, n):
    if m > n:
        m, n = n, m
    p = m * n
    while m != 0:
        r = n % m
        n = m
        m = r
    return (n, p//n)


n1 = int(input("请输入一个正整数："))
n2 = int(input("请输入第二个正整数："))
print(process(m, n))


# 结果
# 输入2，3
# 输出(1, 6)


# 2.编写函数，接收一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。

string = input("请输入一句话：")


def count(input_str):
    words = 0
    number = 0
    blank = 0
    other = 0
    for i in input_str:
        if i.encode().isalpha():
            words += 1
        elif i.isdigit():
            number += 1
        elif i.isspace():
            blank += 1
        else:
            other += 1
    print("数字%d个,字母%d个,空格%d个,其他字符%d个" % (words, number, blank, other))


count(string)

# 结果
# 输入”hello world！“
# 输出数字0个,字母10个,空格1个,其他字符1个