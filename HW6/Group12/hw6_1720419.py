#1 �������ַ�����PHP�滻ΪPython      
best_language = "PHP is the best programming language in the world! "
    print(best_language.replace("PHP", "Python"))
 
#2 ��д���룬��ʾ�û�����1-7�߸����֣��ֱ������һ�����գ���ӡ������������ܼ���
num_input = input("������1-7���֣�")
    print("��������{}".format(num_input))

#3 ����һ���ַ����� Python is the BEST programming Language��
#��дһ��������ʽ�����жϸ��ַ����Ƿ�ȫ��ΪСд��
import re  
str = 'Python is the BEST programming Language��'
an = re.search('^[a-z]+$', str)
if an:
    print("���ַ���ȫ��ΪСд��")
else:
    print("���ַ�����ȫΪСд��")

#4  ��ȡһ���ַ�����Ҫ��ʹ��������ʽ����ȡ���еĵ绰���룬�绰����ĸ�ʽ�ٶ�Ϊ��
#��xxx�� xxx-xxxx��xxx-xxx-xxxx��
import re
str = "�ҵĵ绰������ (173)130-0415,5650-5650-555,731-568-5650"
res = re.findall(r'([(]\d{3}[)]|\d{3})-?(\d{3})-(\d{4})', str)
for each in res:
    print(each[0], each[1], each[2], sep="-")

#5 ����������ʽ�����в�ͬ���ַ����л�ȡָ����ʽ�����ڡ����ڵĸ�ʽΪyyyy-mm-dd��
#'������2022/9/24', '������2017/09/25', '������2012-07-25', '������2020��04��25',
import re
str = "������2022/9/24,������2017/09/25,������2012-07-25,������2020��04��25"
com = re.compile(r'\d{4}-\d{2}-\d{2}')
char = re.findall(com, char)
    print(char)