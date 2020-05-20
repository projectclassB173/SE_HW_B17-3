# 编写一个Python程序，采用SQLite数据库实现通讯录管理功能。 
# 采用SQLite数据库存放个人通讯录，要求存放联系人的姓名、电话、公司、地址； 
# 设计相应的函数完成以下数据库操作： 
# 创建数据库表； 
# 新增联系人； 
# 按姓名查询联系人详细信息； 
# 删除联系人

import sqlite3
conn = sqlite3.connect('D:\\网课\\项目实战\\test.db')
print("Opened database successfully");

conn.execute('''CREATE TABLE USER
(ID INT PRIMARY KEY     NOT NULL, 
NAME           TEXT    NOT NULL,  
TELEPHONE      CHAR(25) NOT NULL,
COMPANY        TEXT    NOT NULL,
ADDRESS        TEXT    NOT NULL);''')
print("Table USER created successfully");

conn.execute("INSERT INTO USER (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
    VALUES (1, 'Gem', 15221281553, 'G公司','普陀')")
conn.execute("INSERT INTO USER (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
    VALUES (2, 'Jasmine', 15921295537, 'J公司','宝山')")
conn.execute("INSERT INTO USER (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
    VALUES (3, 'Sandy', 13764389013, 'S公司','静安')")
conn.commit()
num1=conn.total_changes
print("{0} rows changed in table USER.".format(num1))

conn = sqlite3.connect('D:\\网课\\项目实战\\test.db')
print("Opened database successfully")
cursor1 = conn.execute("SELECT ID,NAME,TELEPHONE,COMPANY,ADDRESS from USER where ID=2")
for row in cursor1:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("TELEPHONE = ", row[2])
   print("COMPANY = ", row[3])
   print("ADDRESS = ", row[4])

conn = sqlite3.connect('D:\\网课\\项目实战\\test.db')
print("Opened database successfully")
conn.execute("delete from USER where COMPANY='S公司'")
conn.commit()
print("Total number of rows updated :", conn.total_changes)
num1=conn.total_changes
print("{0} rows changed in table USER.".format(num1))

conn = sqlite3.connect('D:\\网课\\项目实战\\test.db')
print("Opened database successfully")
conn.execute("UPDATE USER set Company = 'Y公司' where ID=1")
conn.commit()
print("Total number of rows updated :", conn.total_changes)
cursor1 = conn.execute("SELECT ID,NAME,TELEPHONE,COMPANY,ADDRESS from USER where ID=1")
for row in cursor1:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("TELEPHONE = ", row[2])
   print("COMPANY = ", row[3])
   print("ADDRESS = ", row[4])
conn.close()


#结果：
C:\Users\LXYlx\PycharmProjects\Lxy_01\venv\Scripts\python.exe C:/Users/LXYlx/PycharmProjects/Lxy_01/venv/4.py
Opened database successfully
Table USER created successfully
3 rows changed in table USER.
Opened database successfully
ID =  2
NAME =  Jasmine
TELEPHONE =  15921295537
COMPANY =  J公司
ADDRESS =  宝山
Opened database successfully
Total number of rows updated : 1
1 rows changed in table USER.
Opened database successfully
Total number of rows updated : 1
ID =  1
NAME =  Gem
TELEPHONE =  15221281553
COMPANY =  Y公司
ADDRESS =  普陀

Process finished with exit code 0
