# 1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
def Common(x, y):
    if x > y:
        x, y = y, x
    n = x * y
    while x != 0:
        m = y % x
        y = x
        x = m
    return (y, int(n/y))
print(Common(12, 30))

# 运行结果:(3, 30)


# 2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。
def count(s):
    number,letter,space,other = 0,0,0,0
    for i in s:
        if i.isnumber():
            number += 1
        elif i.isletter():
            letter += 1
        elif i.isspace():
            space += 1
        else:
            other += 1
    print('数字有{}个，字母有{}个，空格有{}个，其他有{}个'.format(number,letter,space,other))
count(input("请输入字符串："))

# 运行结果:
请输入字符串：ce4%42v gH fd
数字有3个，字母有7个，空格有2个，其他有1个
