
# ��һ��  �������ַ�����PHP�滻ΪPython

best_language = "PHP is the best programming language in the world! "
print(best_language.replace("PHP","Python"))


# �ڶ��� ��д���룬��ʾ�û�����1 - 7�߸����֣�
# �ֱ������һ�����գ���ӡ������������ܼ���

cus_input = input("������1-7�߸����֣�")
print("��������{}".format(cus_input))


# ������ ����һ���ַ����� Python is the BEST programming Language��
# ��дһ��������ʽ�����жϸ��ַ����Ƿ�ȫ��ΪСд��

import re
best_language = "PHP is the best programming language in the world! "
zfc = '[a-z]+$'  
result = re.search(zfc, best_language) 
if result:
    print('ȫ������Сд')
else:
    print('����ȫ��Сд')


# ������ ��ȡһ���ַ�����Ҫ��ʹ��������ʽ����ȡ���еĵ绰���룬�绰����ĸ�ʽ�ٶ�Ϊ��
# ��xxx�� xxx - xxxx��xxx - xxx - xxxx��

import re
inputString = input('�������ַ���: ')
rule = r'\(\d{3}\)\s\d{3}-\d{4}|\d{3}-\d{3}-\d{4}'  
result = re.findall(rule, inputString)  
for i in range(len(result)):
    print(result[i])


# ������ ����������ʽ�����в�ͬ���ַ����л�ȡָ����ʽ�����ڡ����ڵĸ�ʽΪyyyy - mm - dd��
# '������2022/9/24,������2017/09/25,������2012-07-25,������2020��04��25'

import re
datetext = '������2022/9/24, ������2017/09/25, ������2012-07-25, ������2020��04��25'
result = re.findall(r"(\d{4}-\d{1,2}-\d{1,2})", datetext)
print("".join(result))