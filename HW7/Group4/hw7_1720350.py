'''1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。'''
def h(a,b):
    if a > b:
        a, b = b, a
    c=a*b
    while(b!=0):
        t=a%b
        a=b
        b=t
    return (a,c//a)
print(h(520,1314))

'''2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。'''
def count(str):
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
count(input("请输入一个字符串："))

