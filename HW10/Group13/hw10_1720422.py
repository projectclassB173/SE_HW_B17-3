""""
v编写一个Python程序，采用SQLite数据库实现通讯录管理功能。
v采用SQLite数据库存放个人通讯录，要求存放联系人的姓名、电话、公司、地址；
v设计相应的函数完成以下数据库操作：
n创建数据库表；
n新增联系人；
n按姓名查询联系人详细信息；
n删除联系人
"""
import sqlite3
conn = sqlite3.connect('D:\\temp\\PY\\csl.db')
print("Opened database successfully");

conn.execute('''CREATE TABLE wechat
(ID INT PRIMARY KEY     NOT NULL, 
NAME           TEXT    NOT NULL,  
TELEPHONE      CHAR(15) NOT NULL,
COMPANY        TEXT    NOT NULL,
ADDRESS        TEXT    NOT NULL);''')
print("Table wechat created successfully");

conn.execute("INSERT INTO wechat (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
    VALUES (1, '张三', 123456, '张公司','张地址')")
conn.execute("INSERT INTO wechat (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
    VALUES (2, '李四', 654321, '李公司','李地址')")
conn.execute("INSERT INTO wechat (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
    VALUES (3, '王五', 1234567, '王公司','王地址')")

conn.commit()
num=conn.total_changes
print("{0} rows changed in table test.".format(num))

conn = sqlite3.connect('D:\\temp\\PY\\csl.db')
print("Opened database successfully")
cursor1 = conn.execute("SELECT ID,NAME,TELEPHONE,COMPANY,ADDRESS from wechat where NAME='chen'")
for row in cursor1:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("TELEPHONE = ", row[2])
    print("COMPANY = ", row[3])
    print("ADDRESS = ", row[4])

conn = sqlite3.connect('D:\\temp\\PY\\csl.db')
print("Opened database successfully")
conn.execute("delete from wechat where NAME='chen'")
conn.commit()
print("Total number of rows updated :", conn.total_changes)
num=conn.total_changes
print("{0} rows changed in table USER.".format(num))
conn.close()