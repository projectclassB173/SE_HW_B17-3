#1
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
x = int(input("输入第一个数字: "))
y = int(input("输入第二个数字: "))
print(gys(x, y))


#2
def count(k):
    a = b = c = d = 0;
    for i in k:
        if i.isdigit():
            a = a + 1
        elif i.isalpha():
            b = b + 1
        elif i.isspace():
            c = c + 1
        else:
            d = d + 1
    print("数字{}个，字母{}个，空格{}个，其他字符{}个".format(a, b, c, d))
k = input("输入字符串：")
print(count(k))