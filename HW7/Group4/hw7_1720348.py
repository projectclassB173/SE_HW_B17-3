#1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。

def de(x,y):
    if x>y:
        x, y = y, x
    p=x*y
    while x!=0:
        r=y%x
        y=x
        x=r
    return (y,p//y)

print(de(20,30))


#2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。

def num(str):
    a = b = c = d = 0
    for i in str:
        if i.isdigit():
            a += 1
        elif i.isalpha():
            b += 1
        elif i.isspace():
            c += 1
        else:
            d += 1
    print("数字{}个，字母{}个，空格{}个，其他字符{}个".format(a,b,c,d))

num(input("请输入一个字符串："))

