# 1.ĳ������Ҫ��ȡ��ĸ�����Ϣ,���һ������
#	����ʱ�ֱ������û����롢�������Ա�����,��������,�뽫���ݴ洢Ϊһ���ֵ�.


def personal_info():
    info = dict()
    print("---XX����������Ϣ��---")
    info["����"] = input("����������:")
    info["�Ա�"] = input("�������Ա�:")
    info["����"] = input("����������:")

    return info


# 2.���ݴ洢���ˣ�Ȼ��������˽���:
def print_info(info):
    print("�ҵ�����{},����{}��,�Ա�{},ϲ���ô��롣\n" .format(info["����"], info["����"], info["�Ա�"]))


# 3.��һ���˶���ܸ���Ȥ,ƽ̨��Ҫ������������ߺ���ϵ��ʽ
#	�����û�������ߡ���ϵ��ʽ,��������ӵ�1�д������ֵ�.
def add_info(info):
    print("��һ���˶���ܸ���Ȥ,ƽ̨��Ҫ������������ߺ���ϵ��ʽ.")
    info["���"] = input("���������:")
    info["��ϵ��ʽ"] = input("��������ϵ��ʽ:")
    print("")

    return info


def print_all_info(info):
    print("---������Ϣ---")
    for key in info:
        print("{}:{}" .format(key, info[key]))
    print("")


information = personal_info()
print_info(information)
add_info(information)
print_all_info(information)

# 5.��ǰ��һ���б� li = [11,22,33,22,22,44,55,77,88,99,11] ��ȥ���ظ�Ԫ��֮����ͳ��Ԫ�ص�����
# ����1
li = [11, 22, 33, 22, 22, 44, 55, 77, 88, 99, 11]
li2 = li[:]
for each in li2:
    if li.count(each) != 1:
        li.remove(each)
print("5.��ǰ��һ���б� li = [11,22,33,22,22,44,55,77,88,99,11],��ȥ���ظ�Ԫ��֮����ͳ��Ԫ�ص�����")
print("����1:", len(li))

# ����2
li = [11, 22, 33, 22, 22, 44, 55, 77, 88, 99, 11]
li3 = list()
for each in li:
    if each not in li3:
        li3.append(each)
print("����2:", len(li3))
print("")


# 6.li = [1,2,3,4,5,6,7,8,9] ��ͨ����Ƭ�ó���� [3,6,9]
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
li2 = li[2::3]
print("6.li = [1,2,3,4,5,6,7,8,9] ��ͨ����Ƭ�ó���� [3,6,9]")
print("��Ƭ���:", li2)
print("")


# 7.s = 'python java php',ͨ����Ƭ��ȡ: ��java��
s = 'python java php'
s1 = s[6:11]
print("7.s = 'python java php',ͨ����Ƭ��ȡ: ��java��")
print("��Ƭ���:", s1)