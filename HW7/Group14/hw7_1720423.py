#1.��д����������������������Ϊ����������һ��Ԫ�飬���е�һ��Ԫ��Ϊ���Լ�����ڶ���Ԫ��Ϊ��С��������

def temp(a,b):
    if a>b:
        a, b = b, a
    p=a*b
    while a!=0:
        r=b%a
        b=a
        a=r
    return (b,p//b)
print(temp(2,3))




# 2.��д����������һ���ַ�����Ϊ���������㲢��ӡ�����ַ��������֣���ĸ���ո��Լ������ĸ�����
def num(str):
    x = y = z = m = 0
    for i in str:
        if i.isdigit():
            x += 1
        elif i.isalpha():
            y += 1
        elif i.isspace():
            z += 1
        else:
            m += 1
    print("������{}������ĸ��{}�����ո���{}���������ַ���{}��".format(x,y,z,m))

num(input("������һ���ַ�����"))