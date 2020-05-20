# 编写一个Python程序，采用SQLite数据库实现通讯录管理功能。
# 采用SQLite数据库存放个人通讯录，要求存放联系人的姓名、电话、公司、地址；
# 设计相应的函数完成以下数据库操作：
# 创建数据库表；
# 新增联系人；
# 按姓名查询联系人详细信息；
# 删除联系人；


# 创建数据库表；
import sqlite3

conn = sqlite3.connect('D:\\djb\\connect.db')
print("Opened database successfully");
conn.execute('''CREATE TABLE CONTACT
(ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
PHONE TEXT NOT NULL,
COMPANY TEXT NOT NULL,
ADDRESS TEXT NOT NULL);''')
print("表顺利创建");

# 新增联系人；


conn = sqlite3.connect('D:\\djb\\connect.db')
print("Opened database successfully");
conn.execute("INSERT INTO CONTACT (ID,NAME,PHONE,COMPANY,ADDRESS) \
VALUES (01, 'njw', '137137137', 'wow','shanghai')")
conn.execute("INSERT INTO CONTACT (ID,NAME,PHONE,COMPANY,ADDRESS) \
VALUES (02, 'lkj', '1357924680', 'knn','北京')")
conn.execute("INSERT INTO CONTACT (ID,NAME,PHONE,COMPANY,ADDRESS) \
VALUES (03, '小熊维尼', '4568128574', 'xct','北京')")
conn.commit()
num1 = conn.total_changes
print("{0} 条记录插入.".format(num1))

# 按姓名查询联系人详细信息；


conn = sqlite3.connect('D:\\djb\\connect.db')
print("Opened database successfully")
cursor1 = conn.execute("SELECT ID,NAME,PHONE,COMPANY,ADDRESS from CONTACT where NAME = 'njw'")
for row in cursor1:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("PHONE = ", row[2])
    print("COMPANY = ", row[3])
    print("ADDRESS = ", row[4])


# 删除联系人；


conn = sqlite3.connect('D:\\djb\\connect.db')
print("Opened database successfully")
conn.execute("delete from CONTACT where NAME='njw'")
conn.commit()
print("更新的行数:", conn.total_changes)
num1 = conn.total_changes
print("{0} 条记录已删除.".format(num1))

conn.close()