##1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。

def process(m, n):
    if m > n:
        m, n = n, m
    p = m * n
    while m != 0:
        r = n % m
        n = m
        m = r
    return (n, p//n)


n1 = int(input("请输入一个正整数："))
n2 = int(input("请输入第二个正整数："))
print(process(m, n))


##2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。

def gs(*string):
    yw,kg,sz,qt=0,0,0,0
    for str1 in string:
    for i in str1:
	if('0'<=i<='9'):
                     sz=sz+1
	elif 'a'<=i<='z' or 'A'<=i<='Z':
                     yw=yw+1
	        elif i==' ':
                            kg=kg+1
	else:
	            qt=qt+1
	return (yw,kg,sz,qt)
                      gs("123   asbJSA#$%")
                         (6, 3, 3, 3)
                      gs("123456789","!@#$%^&*(","         ","ABCdefghi")
                         (9, 9, 9, 9)
