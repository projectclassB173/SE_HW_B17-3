#1.

def demo(m,n):
    p = m*n
    while m%n != 0:
        m,n = n,m%n
    return(n,p//n)

print(demo(12, 30))

#运行结果：(6, 60)


#2.

def num(str1):
    a = b = c = d = 0
    for i in str1:
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

#运行结果：请输入一个字符串：1a b
#数字1个，字母2个，空格1个，其他字符0个