# 1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
def gcm(a, b):
	assert a > 0 and b > 0,'parameters must be greater than 0.'
	if a >= b:
		if a % b == 0:
			return b
		else:
			return gcm(b, a - b)
	else:
		return gcm(b, a)

def lcm(a, b):
	assert a > 0 and b > 0,'parameters must be greater than 0.'
	return a * b / gcm(a, b)
# 2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。
def count(x):
    a = b = c = d = 0
    for i in x:
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
