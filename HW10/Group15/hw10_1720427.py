'''题目为：
编写一个Python程序，采用SQLite数据库实现通讯录管理功能。
采用SQLite数据库存放个人通讯录，要求存放联系人的姓名、电话、公司、地址；
设计相应的函数完成以下数据库操作：
    创建数据库表；
    新增联系人；
    按姓名查询联系人详细信息；
    删除联系人；
'''
import sqlite3
conn = sqlite3.connect('C:\\Users\\HP\\Desktop\\项目实战\\1720427.db')
print("数据库已经被成功打开");

#创建
conn.execute('''CREATE TABLE USER 
       (ID number PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       PHONE         CHAR(20)   NOT NULL,
       COMPANY       TEXT   NOT NULL,
       ADDRESS       TEXT   NOT NULL);''')
print("数据库表创建成功");

#插入
conn.execute("INSERT INTO USER (ID,NAME,PHONE,COMPANY,ADDRESS) \
    VALUES (1, 'kyf', 18081151532,'酒店','静安寺')")

conn.execute("INSERT INTO USER (ID,NAME,PHONE,COMPANY,ADDRESS) \
    VALUES (2, 'zwh', 18694567962,'建桥学院','滴水湖')")

conn.execute("INSERT INTO USER (ID,NAME,PHONE,COMPANY,ADDRESS) \
    VALUES (3, 'kk', 17756233641,'电影院','三林')")
conn.commit()
num1=conn.total_changes
print("{0} rows changed in table USER.".format(num1))
print("已经成功打开数据表")

#查询
import sqlite3
conn = sqlite3.connect('C:\\Users\\HP\\Desktop\\项目实战\\1720427.db')
data = conn.execute("SELECT ID,NAME,PHONE,COMPANY,ADDRESS from USER where ID in (1,2,3)")
for row in data:
   print("ID号为 ", row[0])
   print("姓名是 ", row[1])
   print("电话是 ", row[2])
   print("公司是 ", row[3])
   print("地址是 ", row[4])

#删除
import sqlite3
conn = sqlite3.connect('C:\\Users\\HP\\Desktop\\项目实战\\1720427.db')
conn.execute("delete from USER where COMPANY='电影院'")
conn.commit()
print("删除后，数据更新为:", conn.total_changes)
num1=conn.total_changes
print("{0} rows changed in table USER.".format(num1))

#更改
import sqlite3
conn = sqlite3.connect('C:\\Users\\HP\\Desktop\\项目实战\\1720427.db')
conn.execute("UPDATE USER set ADDRESS = '阿里巴巴' where ID=3")
conn.commit()
print("更改后，数据更新为", conn.total_changes)
data = conn.execute("SELECT ID,NAME,PHONE,COMPANY,ADDRESS from USER where ID=3")
for row in data:
   print("ID号为 ", row[0])
   print("姓名是 ", row[1])
   print("电话是 ", row[2])
   print("公司是 ", row[3])
   print("地址是 ", row[4])
conn.close()

"""
结果是：
"D:\Program Files\PyCharm 2020.1.1\workspace\Scripts\python.exe" "D:/Program Files/PyCharm 2020.1.1/Projects/hw10_1720427.py"
数据库已经被成功打开
数据库表创建成功
3 rows changed in table USER.
已经成功打开数据表
ID号为  1
姓名是  kyf
电话是  18081151532
公司是  酒店
地址是  静安寺
ID号为  2
姓名是  zwh
电话是  18694567962
公司是  建桥学院
地址是  滴水湖
ID号为  3
姓名是  kk
电话是  17756233641
公司是  电影院
地址是  三林
删除后，数据更新为: 1
1 rows changed in table USER.
更改后，数据更新为 0

Process finished with exit code 0
"""