#1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
def gys(x, y):
    if x > y:
        key = y
    else:
        key = x
    for i in range(1, key + 1):
        if (x % i == 0) and (y % i == 0):
            number1 = i
    number2 = (x * y) / number1
    return number1, number2


num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))
print(gys(num1, num2))


#2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。
def count(str1):
    a = 0;
    b = 0;
    c = 0;
    d = 0;
    for i in str1:
        if i.isdigit():
            a += 1
        elif i.isalpha():
            b += 1
        elif i.isspace():
            c += 1
        else:
            d += 1
    print("数字{}个，字母{}个，空格{}个，其他字符{}个".format(a, b, c, d))


k = input("输入字符串：")
print(count(k))
