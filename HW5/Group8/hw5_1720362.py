# ��Ŀ<1>
name = input("����������")
sex = input("�����Ա�")
age = input("�������䣺")
dic = {}
dic.update({"����": name, "�Ա�": sex, "����": age})
print(dic)

# ��Ŀ<2>
print("�ҵ�����{},���� {} �꣬�Ա� {},ϲ���ô���".format(dic["����"], dic["����"], dic["�Ա�"]))

# ��Ŀ<3>
height = input("��������ߣ�")
phone = input("��������ϵ��ʽ��")
dic.update({"���": height, "��ϵ��ʽ": phone})
print(dic)

# ��Ŀ<4>
for i in dic:
    print("{}:{}".format(i,dic[i]))

# ��Ŀ<5>
li = [11, 22, 33, 22, 22, 44, 55, 77, 88, 99, 11]
s = set(li)
li = list(s)
print(li)
print(len(li))

# ��Ŀ<6>
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("�����", li[2::3])

# ��Ŀ<7>
s = 'python java php'
print("�����", "\'"+s[7:11]+"\'")