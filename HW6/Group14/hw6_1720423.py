'''
1���������ַ�����PHP�滻ΪPython
best_language = "PHP is the best programming language in the world!"
2����д���룬��ʾ�û�����1-7�߸����֣��ֱ������һ�����գ���ӡ������������ܼ���
3������һ���ַ����� Python is the BEST programming Language!
��дһ��������ʽ�����жϸ��ַ����Ƿ�ȫ��ΪСд��
4����ȡһ���ַ�����Ҫ��ʹ��������ʽ����ȡ���еĵ绰���룬�绰����ĸ�ʽ�ٶ�Ϊ��
(xxx)xxx-xxxx��xxx-xxx-xxxx��
5������������ʽ�����в�ͬ���ַ����л�ȡָ����ʽ�����ڡ����ڵĸ�ʽΪyyyy-mm-dd��
'������2022/9/24', '������2017/09/25', '������2012-07-25', '������2020��04��25'��
'''

# 1.�������ַ�����PHP�滻ΪPython
best_language = "PHP is the best programming language in the world! "
print(best_language.replace("PHP", "Python"))
print("----------")

# 2.��д���룬��ʾ�û�����1 - 7
# �߸����֣��ֱ������һ�����գ���ӡ������������ܼ���
day = ["һ", "��", "��", "��", "��", "��", "��"]
num = int(input("����������1-7:"))
print("��������{}" .format(day[num-1]))
print("----------")

# 3.����һ���ַ����� Python is the BEST programming Language��
# ��дһ��������ʽ�����жϸ��ַ����Ƿ�ȫ��ΪСд��
import re
string = "Python is the BEST programming Language��"
if len(re.findall("[A-Z]", string))>0:
    print("ȫΪСд")
else:
    print("��ȫΪСд")


# 4.��ȡһ���ַ�����Ҫ��ʹ��������ʽ����ȡ���еĵ绰���룬�绰����ĸ�ʽ�ٶ�Ϊ��
# ��xxx�� xxx - xxxx��xxx - xxx - xxxx��
import re
s1 = "Phone number is (0215)123-1234 , 056-234-4567 , 074-457-9878 , (020)475-7542"
result = re.findall(r'([(]\d{3}[)]|\d{3})-?(\d{3})-(\d{4})', s1)
for each in result:
    print(each[0], each[1], each[2], sep="-")
print("----------")

# 5.����������ʽ�����в�ͬ���ַ����л�ȡָ����ʽ�����ڡ����ڵĸ�ʽΪyyyy - mm - dd��
import re
s = '������2022/9/24,������2017/09/25,������2012-07-25,������2020��04��25'
d = re.findall(r'\d{4}-\d?\d-\d?\d', str1)
for each in d:
    print(each)
print("-----END-----")
    
