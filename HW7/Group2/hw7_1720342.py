#1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
def maxgys(a, b):
	assert a > 0 and b > 0,'parameters must be greater than 0.'
	if a >= b:
		if a % b == 0:
			return b
		else:
			return maxgys(b, a - b)
	else:
		return maxgys(b, a)

def mingbs(a, b):
	assert a > 0 and b > 0,'parameters must be greater than 0.'
	return a * b / maxgys(a, b)

a = int(input("第一个正整数: "))
b = int(input("第二个正整数: "))
print(maxgys(a, b))
print(mingbs(a, b))

#2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。
def count(s):
  alpha,num,space,other=0,0,0,0
  for i in s:
    if i.isalpha():
        alpha+=1
    elif i.isdigit():
        num+=1
    elif i.isspace():
        space+=1
    else:
        other+=1
  print('英文字符数{},数字字符数{},空格字符数{},其他字符数{}'.format(alpha,num,space,other))
count(input("请输入一个字符串："))