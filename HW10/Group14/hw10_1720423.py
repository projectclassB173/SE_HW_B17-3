'''
��дһ��Python���򣬲���SQLite���ݿ�ʵ��ͨѶ¼�����ܡ�
����SQLite���ݿ��Ÿ���ͨѶ¼��Ҫ������ϵ�˵��������绰����˾����ַ��
�����Ӧ�ĺ�������������ݿ������
    �������ݿ��
    ������ϵ�ˣ�
    ��������ѯ��ϵ����ϸ��Ϣ��
    ɾ����ϵ�ˣ�
'''

import sqlite3
conn = sqlite3.connect('D:\\��Ŀʵս\\Դ��\\test.db')
print("Opened database successfully");
conn.execute('''CREATE TABLE test 
(ID INT PRIMARY KEY     NOT NULL, 
NAME           TEXT    NOT NULL,  
TELEPHONE      CHAR(15) NOT NULL,
COMPANY        TEXT    NOT NULL,
ADDRESS        TEXT    NOT NULL);''')
print("Table USER created successfully");
conn.execute("INSERT INTO test (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
    VALUES (1, '��ΰ��', 111720423, '�Ϻ�����ѧԺ','��ɽ��')")
conn.execute("INSERT INTO test (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
    VALUES (2, '��ΰ��', 211720423, '�Ϻ����´�ѧ','������')")
conn.execute("INSERT INTO test (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
    VALUES (3, '��ΰ��', 311720423, '�Ϻ���ѧ','��ɽ��')")
conn.execute("INSERT INTO test (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
    VALUES (4, 'С��', 411720423, '�Ϻ�������ѧ','�����')")
conn.commit()
num=conn.total_changes
print("{0} rows changed in table test.".format(num))
conn = sqlite3.connect('D:\\��Ŀʵս\\Դ��\\test.db')
print("Opened database successfully")
cursor1 = conn.execute("SELECT ID,NAME,TELEPHONE,COMPANY,ADDRESS from test where NAME='��ΰ��'")
for row in cursor1:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("TELEPHONE = ", row[2])
    print("COMPANY = ", row[3])
    print("ADDRESS = ", row[4])
conn.execute("delete from test where NAME='��ΰ��'")
conn.commit()
print("Total number of rows updated :", conn.total_changes)
num=conn.total_changes
print("{0} rows changed in table USER.".format(num))