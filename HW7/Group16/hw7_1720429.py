#1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
def a(x,y):
    if x>y:
        x,y=y,x
        p=x*y
        while x!=0:
            q=y%x
            y=x
            x=q
    return (int (p/y),y)
print(a(1720,429))

#2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。
def a(x):
    dig = 0
    sp =0
    cha =0
    q=0
    for i in x:
        if i.isdigit():      # isdigit 判断有没有数字
            dig += 1
        elif i.isspace():    # isspace 判断有没有空格
            sp += 1
        elif i.isalpha():    #isalpha 判断有没有字符
            cha += 1
        else:
            q += 1
            return(dig,sp,cha,q)

r = a("1720429 python!")
print(r)
