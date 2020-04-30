#1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。

def temp(a,b):
    if a>b:
        a, b = b, a
    p=a*b
    while a!=0:
        r=b%a
        b=a
        a=r
    return (b,p//b)
print(temp(2,3))




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
    print("数字有{}个，字母有{}个，空格有{}个，其他字符有{}个".format(x,y,z,m))

num(input("请输入一个字符串："))