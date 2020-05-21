'''
编写一个Python程序，采用SQLite数据库实现通讯录管理功能。
采用SQLite数据库存放个人通讯录，要求存放联系人的姓名、电话、公司、地址；
设计相应的函数完成以下数据库操作：
    创建数据库表；
    新增联系人；
    按姓名查询联系人详细信息；
    删除联系人；
'''

import sqlite3
conn = sqlite3.connect('D:\\项目实战\\源码\\test.db')
print("Opened database successfully");
conn.execute('''CREATE TABLE test 
(ID INT PRIMARY KEY     NOT NULL, 
NAME           TEXT    NOT NULL,  
TELEPHONE      CHAR(15) NOT NULL,
COMPANY        TEXT    NOT NULL,
ADDRESS        TEXT    NOT NULL);''')
print("Table USER created successfully");
conn.execute("INSERT INTO test (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
    VALUES (1, '沈伟超', 111720423, '上海建桥学院','宝山区')")
conn.execute("INSERT INTO test (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
    VALUES (2, '沈伟走', 211720423, '上海海事大学','静安区')")
conn.execute("INSERT INTO test (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
    VALUES (3, '沈伟起', 311720423, '上海大学','宝山区')")
conn.execute("INSERT INTO test (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
    VALUES (4, '小方', 411720423, '上海复旦大学','虹口区')")
conn.commit()
num=conn.total_changes
print("{0} rows changed in table test.".format(num))
conn = sqlite3.connect('D:\\项目实战\\源码\\test.db')
print("Opened database successfully")
cursor1 = conn.execute("SELECT ID,NAME,TELEPHONE,COMPANY,ADDRESS from test where NAME='沈伟超'")
for row in cursor1:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("TELEPHONE = ", row[2])
    print("COMPANY = ", row[3])
    print("ADDRESS = ", row[4])
conn.execute("delete from test where NAME='沈伟超'")
conn.commit()
print("Total number of rows updated :", conn.total_changes)
num=conn.total_changes
print("{0} rows changed in table USER.".format(num))