# 1.��д����������������������Ϊ����������һ��Ԫ�飬���е�һ��Ԫ��Ϊ���Լ�����ڶ���Ԫ��Ϊ��С��������

def demo(m,n):
    if m>n:
        m, n = n, m
    p = m*n
    while m!= 0:
        r=n%m
        n=m
        m=r
    return(n,p//n)

print(demo(5, 25))


# 2.��д����������һ���ַ�����Ϊ���������㲢��ӡ�����ַ��������֣���ĸ���ո��Լ������ĸ�����

def count(str1):
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
    print("����{}������ĸ{}�����ո�{}���������ַ�{}��".format(a,b,c,d))

count(input("������һ���ַ�����"))
