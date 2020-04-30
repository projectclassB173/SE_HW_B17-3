# 1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
def number(g, j):
    if g > j:
        g, j = j,g
    s = g * j
    while g != 0:
        r = j % g
        j = g
        g = r
    return j, int(s / j)
            

g = int(input("请输入第一个正整数g=:"))
j = int(input("请输入第二个正整数j=:"))
print(number(g, j))


# 运行结果：
# 请输入第一个正整数g=:12
# 请输入第二个正整数j=:16
# (4, 48)

# 2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。
def count1(s):
    num = 0
    space = 0
    digit = 0
    others = 0
    for i in s:
        if i.isdigit():
            digit = digit + 1
        elif i.isspace():
            space = space + 1
        elif i.isalpha():
            num = num + 1
        else:
            others = others + 1
    print("数字:%d,空格:%d,字母:%d,其它:%d" % (num, space, digit, others))


s = input("请输入一个字符串：")
count1(s)
# 运行结果；
# 请输入一个字符串：111 aaa ...
# 数字:3,空格:2,字母:3,其它:3
