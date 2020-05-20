"""
编写一个Python程序，采用SQLite数据库实现通讯录管理功能。
采用SQLite数据库存放个人通讯录，要求存放联系人的姓名、电话、公司、地址；
设计相应的函数完成以下数据库操作：
创建数据库表；
新增联系人；
按姓名查询联系人详细信息；
删除联系人；
"""

import sqlite3
# 下面的代码显示如何连接到一个现有的数据库。如果数据库不存在，那么它就会被创建，最后将返回一个数据库对象
conn = sqlite3.connect('D:\\GG\\testhw10.db')
c = conn.cursor()
print("成功打开数据库")
c.execute('''CREATE TABLE USER
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       PHONE         CHAR(15)    NOT NULL,
       COMPANY       CHAR(50)   NOT NULL,
       ADDRESS        CHAR(50)      NOT NULL);''')      # testhw10.db 中创建 USER 表
print("成功创建表")
# 以下代码显示如何在上面创建的 USER 表中创建详细信息
c.execute("INSERT INTO USER (ID,NAME,PHONE,COMPANY,ADDRESS) \
      VALUES (1,'KK', '13585890317', '天下无敌有限公司','上海宝山')")

c.execute("INSERT INTO USER (ID,NAME,PHONE,COMPANY,ADDRESS) \
      VALUES (2,'XX', '18217179680', '人生无限有限公司', '上海浦东' )")

c.execute("INSERT INTO USER (ID,NAME,PHONE,COMPANY,ADDRESS) \
      VALUES (3,'人五', '12345678901', 'W公司', '成都' )")

conn.execute("INSERT INTO USER (ID,NAME,PHONE,COMPANY,ADDRESS) \
      VALUES (4,'微微', '13671704767', 'R公司', '新疆' )")
print("记录创建成功")
#下面的 Python 程序显示了如何从前面创建的 USER 表中获取并显示记录
cursor = c.execute("SELECT ID,NAME,PHONE,COMPANY,ADDRESS  from USER")
for row in cursor:
   print("查询数据库中NAME = ", row[1])
   print("PHONE = ", row[2])
   print("COMPANY = ", row[3])
   print("ADDRESS = ", row[4])
print("操作成功完成")
#以下代码显示了如何使用 DELETE 语句删除任何记录，然后从 USER 表中获取并显示剩余的记录
c.execute("DELETE from USER where ID=2;")
conn.commit()
print("Total number of rows deleted :", conn.total_changes)
cursor = conn.execute("SELECT ID,NAME,PHONE,COMPANY,ADDRESS  from USER where NAME ='人五'")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("PHONE = ", row[2])
   print("COMPANY = ", row[3], "\n")
   print("ADDRESS = ", row[4], "\n")

print("操作成功完成")
conn.close()

"""
C:\Users\Administrator\PycharmProjects\untitled\venv\Scripts\python.exe D:/GG/hw10.py
成功打开数据库
成功创建表
记录创建成功
ID =  人五
NAME =  人五
PHONE =  12345678901
COMPANY =  W公司
ADDRESS =  成都
操作成功完成
Total number of rows deleted : 5
ID =  1
NAME =  KK
PHONE =  13585890317
COMPANY =  天下无敌有限公司 

ADDRESS =  上海宝山 

ID =  3
NAME =  人五
PHONE =  12345678901
COMPANY =  W公司 

ADDRESS =  成都 

ID =  4
NAME =  微微
PHONE =  13671704767
COMPANY =  R公司 

ADDRESS =  新疆 

操作成功完成
"""
