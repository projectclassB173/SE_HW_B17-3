# 1.��д����������������������Ϊ����������һ��Ԫ�飬���е�һ��Ԫ��Ϊ���Լ�����ڶ���Ԫ��Ϊ��С��������

def process(m, n):
    if m > n:
        m, n = n, m
    p = m * n
    while m != 0:
        r = n % m
        n = m
        m = r
    return (n, p//n)


n1 = int(input("������һ����������"))
n2 = int(input("������ڶ�����������"))
print(process(m, n))


# 2.��д����������һ���ַ�����Ϊ���������㲢��ӡ�����ַ��������֣���ĸ���ո��Լ������ĸ�����

string = input("������һ�仰��")

def count(input_str):
    words = 0
    number = 0
    blank = 0
    other = 0
    for i in input_str:
        if i.encode().isalpha():
            words += 1
        elif i.isdigit():
            number += 1
        elif i.isspace():
            blank += 1
        else:
            other += 1
    print("����%d��,��ĸ%d��,�ո�%d��,�����ַ�%d��" % (words, number, blank, other))


count(string)
