"""
��дһ��Python���򣬲���SQLite���ݿ�ʵ��ͨѶ¼�����ܡ�
����SQLite���ݿ��Ÿ���ͨѶ¼��Ҫ������ϵ�˵��������绰����˾����ַ��
�����Ӧ�ĺ�������������ݿ������
�������ݿ��
������ϵ�ˣ�
��������ѯ��ϵ����ϸ��Ϣ��
ɾ����ϵ�ˣ�
"""

import sqlite3
# ����Ĵ�����ʾ������ӵ�һ�����е����ݿ⡣������ݿⲻ���ڣ���ô���ͻᱻ��������󽫷���һ�����ݿ����
conn = sqlite3.connect('D:\\GG\\testhw10.db')
c = conn.cursor()
print("�ɹ������ݿ�")
c.execute('''CREATE TABLE USER
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       PHONE         CHAR(15)    NOT NULL,
       COMPANY       CHAR(50)   NOT NULL,
       ADDRESS        CHAR(50)      NOT NULL);''')      # test.db �д��� USER ��
print("�ɹ�������")
# ���´�����ʾ��������洴���� USER ���д�����ϸ��Ϣ
c.execute("INSERT INTO USER (ID,NAME,PHONE,COMPANY,ADDRESS) \
      VALUES (1,'KK', '13585890317', '�����޵����޹�˾','�Ϻ���ɽ')")

c.execute("INSERT INTO USER (ID,NAME,PHONE,COMPANY,ADDRESS) \
      VALUES (2,'XX', '18217179680', '�����������޹�˾', '�Ϻ��ֶ�' )")

c.execute("INSERT INTO USER (ID,NAME,PHONE,COMPANY,ADDRESS) \
      VALUES (3,'����', '12345678901', 'W��˾', '�ɶ�' )")

conn.execute("INSERT INTO USER (ID,NAME,PHONE,COMPANY,ADDRESS) \
      VALUES (4,'΢΢', '13671704767', 'R��˾', '�½�' )")
conn.commit()
print("��¼�����ɹ�")
#����� Python ������ʾ����δ�ǰ�洴���� USER ���л�ȡ����ʾ��¼
cursor = c.execute("SELECT ID,NAME,PHONE,COMPANY,ADDRESS  from USER")
for row in cursor:
   print("��ѯ���ݿ���NAME = ", row[1])
   print("PHONE = ", row[2])
   print("COMPANY = ", row[3])
   print("ADDRESS = ", row[4])
print("�����ɹ����")

c.execute("DELETE from USER where ID=2;")
conn.commit()
print("Total number of rows deleted :", conn.total_changes)

cursor = conn.execute("SELECT ID,NAME,PHONE,COMPANY,ADDRESS  from USER")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("PHONE = ", row[2])
   print("COMPANY = ", row[3], "\n")
   print("ADDRESS = ", row[4], "\n")

print("�����ɹ����")
conn.close()

"""
C:\Users\Administrator\PycharmProjects\untitled\venv\Scripts\python.exe D:/GG/hw10.py
�ɹ������ݿ�
�ɹ�������
��¼�����ɹ�
��ѯ���ݿ���NAME =  KK
PHONE =  13585890317
COMPANY =  �����޵����޹�˾
ADDRESS =  �Ϻ���ɽ
��ѯ���ݿ���NAME =  XX
PHONE =  18217179680
COMPANY =  �����������޹�˾
ADDRESS =  �Ϻ��ֶ�
��ѯ���ݿ���NAME =  ����
PHONE =  12345678901
COMPANY =  W��˾
ADDRESS =  �ɶ�
��ѯ���ݿ���NAME =  ΢΢
PHONE =  13671704767
COMPANY =  R��˾
ADDRESS =  �½�
�����ɹ����
Total number of rows deleted : 5
ID =  1
NAME =  KK
PHONE =  13585890317
COMPANY =  �����޵����޹�˾ 

ADDRESS =  �Ϻ���ɽ 

ID =  3
NAME =  ����
PHONE =  12345678901
COMPANY =  W��˾ 

ADDRESS =  �ɶ� 

ID =  4
NAME =  ΢΢
PHONE =  13671704767
COMPANY =  R��˾ 

ADDRESS =  �½� 

�����ɹ����
"""
