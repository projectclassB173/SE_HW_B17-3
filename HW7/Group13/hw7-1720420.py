# 1.��д����������������������Ϊ����������һ��Ԫ�飬���е�һ��Ԫ��Ϊ���Լ�����ڶ���Ԫ��Ϊ��С��������
import math


def Calculation(a, b):
    r = math.gcd(a, b)
    return r, (a * b) // r


print(Calculation(30, 42))



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
    print("����{}������ĸ{}�����ո�{}���������ַ�{}��".format(x,y,z,m))

num(input("������һ���ַ�����"))