# 编写一个Python程序，采用SQLite数据库实现通讯录管理功能。 
# 采用SQLite数据库存放个人通讯录，要求存放联系人的姓名、电话、公司、地址； 
# 设计相应的函数完成以下数据库操作： 
# 创建数据库表； 
# 新增联系人； 
# 按姓名查询联系人详细信息； 
# 删除联系人

import sqlite3 
conn = sqlite3.connect('C:\\每周作业\\zzjb.db') 
print("Opened database successfully");

conn.execute('''CREATE TABLE addressbook 
(ID INT PRIMARY KEY     NOT NULL, 
NAME           TEXT    NOT NULL,  
TELEPHONE      CHAR(50) NOT NULL,
COMPANY        TEXT    NOT NULL,
ADDRESS        TEXT    NOT NULL);''') 
print("Table USER created successfully");

conn.execute("INSERT INTO addressbook (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
    VALUES (1, 'zjb', 12819837441, 'z公司','浦东')")
conn.execute("INSERT INTO addressbook (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
    VALUES (2, 'cyc', 18129328324, 'c公司','黄埔')") 
conn.commit() 
num1=conn.total_changes 
print("{0} rows changed in table addressbook.".format(num1))   

conn = sqlite3.connect('C:\\每周作业\\zzjb.db') 
print("Opened database successfully") 
cursor1 = conn.execute("SELECT ID,NAME,TELEPHONE,COMPANY,ADDRESS from addressbook where NAME='zjb'") 
for row in cursor1: 
    print("ID = ", row[0]) 
    print("NAME = ", row[1]) 
    print("TELEPHONE = ", row[2]) 
    print("COMPANY = ", row[3])
    print("ADDRESS = ", row[4])

conn.execute("delete from addressbook where NAME='cyc'") 
conn.commit() 
print("Total number of rows updated :", conn.total_changes) 
num1=conn.total_changes 
print("{0} rows changed in table USER.".format(num1)) 
