# 1.��д����������������������Ϊ����������һ��Ԫ�飬���е�һ��Ԫ��Ϊ���Լ�����ڶ���Ԫ��Ϊ��С��������

import math

def num(m,n):
	a = math.gcd(m, n)
	return a, (m * n)// j
print (num(18,40))


# 2.��д����������һ���ַ�����Ϊ���������㲢��ӡ�����ַ��������֣���ĸ���ո��Լ������ĸ�����

def num(n1):
    a = b = c = d = 0
    for i in n1:
        if i.isdigit():
            a += 1
        elif i.isalpha():
            b += 1
        elif i.isspace():
            c += 1
        else:
            d += 1
    print("����{}������ĸ{}�����ո�{}���������ַ�{}��".format(a,b,c,d))
num(input("������һ���ַ�����"))