＃1。编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。

def  demo（m，n）：
    如果 m > n：
        m，n  =  n，m
    p = m * n
    而 m ！= 0：
        r = n ％m
        n = 米
        m = r
    return（n，p // n）
打印（演示（2，3））

＃2。编写函数，接受一个字符串作为参数，计算并打印并插入串行中数字，字母，空格，以及其他的个数。

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
