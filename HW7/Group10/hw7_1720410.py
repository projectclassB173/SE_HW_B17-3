#1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。

def demo(a,b):
    c = a*b
    while a%b != 0:
        a,b = b,a%b
    return(b,c//b)
print(demo(4,16))

#2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。
def str_number(str_num):
    a = 0
    b = 0
    c = 0
    d = 0
    for i in str_num:
        if i.isdigit() == True:
            a += 1
        elif i.isalpha() == True:
            b += 1
        elif i.isspace() == True:
            c += 1
        else:
            d += 1
    print("数字有%d个"%a)
    print("字母有%d个"%b)
    print("空隔有%d个" %c)
    print("其它有%d个" %d)

str_num = input("请输入字符串:")
str_number(str_num)
