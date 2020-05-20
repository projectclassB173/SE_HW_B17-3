# 编写一个Python程序，采用SQLite数据库实现通讯录管理功能。 
# 采用SQLite数据库存放个人通讯录，要求存放联系人的姓名、电话、公司、地址； 
# 设计相应的函数完成以下数据库操作： 
# 创建数据库表； 
# 新增联系人； 
# 按姓名查询联系人详细信息； 
# 删除联系人；


# 创建数据库表；
import sqlite3

conn = sqlite3.connect('D:\\1720419\\xiangmushizhan\\通讯录管理\\venv\\contacter.db')
print("Opened database successfully");
conn.execute('''CREATE TABLE CONTACTER
(ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
PHONENUMBER TEXT NOT NULL,
COMPANY TEXT NOT NULL,
ADDRESS TEXT NOT NULL);''')
print("Table CONTACTER created successfully");
# Opened database successfully
# Table CONTACTER created successfully

# 新增联系人；
import sqlite3

conn = sqlite3.connect('D:\\1720419\\xiangmushizhan\\通讯录管理\\venv\\contacter.db')
print("Opened database successfully");
conn.execute("INSERT INTO CONTACTER (ID,NAME,PHONENUMBER,COMPANY,ADDRESS) \
VALUES (001, 'Tom', '13813838438', 'tooomy','长乐路15号')")
conn.execute("INSERT INTO CONTACTER (ID,NAME,PHONENUMBER,COMPANY,ADDRESS) \
VALUES (002, 'Jerry', '13913939439', 'Jeeery','宛平南路60号')")
conn.execute("INSERT INTO CONTACTER (ID,NAME,PHONENUMBER,COMPANY,ADDRESS) \
VALUES (003, 'hori', '13004155749', 'hooori','沪青平公路8808号')")
conn.execute("INSERT INTO CONTACTER (ID,NAME,PHONENUMBER,COMPANY,ADDRESS) \
VALUES (004, 'Barry', '114', 'baaary','广富林路77号')")
conn.commit()
num1 = conn.total_changes
print("{0} rows changed in table CONTACTER.".format(num1))
# Opened database successfully
# 4 rows changed in table CONTACTER.

# 按姓名查询联系人详细信息；
import sqlite3

conn = sqlite3.connect('D:\\1720419\\xiangmushizhan\\通讯录管理\\venv\\contacter.db')
print("Opened database successfully")
cursor1 = conn.execute("SELECT ID,NAME,PHONENUMBER,COMPANY,ADDRESS from CONTACTER where NAME = 'hori'")
for row in cursor1:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("PHONENUMBER = ", row[2])
    print("COMPANY = ", row[3])
    print("ADDRESS = ", row[4])
# Opened database successfully
# ID =  3
# NAME =  hori
# PHONENUMBER =  13004155749
# COMPANY =  hooori
# ADDRESS =  沪青平公路8808号

# 删除联系人；
import sqlite3

conn = sqlite3.connect('D:\\1720419\\xiangmushizhan\\通讯录管理\\venv\\contacter.db')
print("Opened database successfully")
conn.execute("delete from CONTACTER where NAME='hori'")
conn.commit()
print("Total number of rows updated :", conn.total_changes)
num1 = conn.total_changes
print("{0} rows changed in table USER.".format(num1))
# Opened database successfully
# Total number of rows updated : 1
# 1 rows changed in table USER.


