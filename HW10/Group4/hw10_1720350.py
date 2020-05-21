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
conn = sqlite3.connect('D:\\大三下\\github\\作业\\第十次作业 增删改查\\1720350.db')
print("数据库已经被成功的打开");

#创建
conn.execute('''CREATE TABLE USER
(ID INT PRIMARY KEY     NOT NULL, 
NAME           TEXT    NOT NULL,  
PHONE      CHAR(25) NOT NULL,
COMPANY        TEXT    NOT NULL,
ADDRESS        TEXT    NOT NULL);''')
print("数据库表创建成功");

#插入
conn.execute("INSERT INTO USER (ID,NAME,PHONE,COMPANY,ADDRESS) \
    VALUES (1, '小a', 12345678915, '出租公司','人民广场')")

conn.execute("INSERT INTO USER (ID,NAME,PHONE,COMPANY,ADDRESS) \
    VALUES (2, '小b', 52663489112, '建桥学院','滴水湖')")

conn.execute("INSERT INTO USER (ID,NAME,PHONE,COMPANY,ADDRESS) \
    VALUES (3, '小c', 52436125489, '大酒店','徐家汇')")
conn.commit()
num1=conn.total_changes
print("{0} rows changed in table USER.".format(num1))
print("已经成功打开数据表")

#查询
import sqlite3
conn = sqlite3.connect('D:\\大三下\\github\\作业\\第十次作业 增删改查\\1720350.db')
data = conn.execute("SELECT ID,NAME,PHONE,COMPANY,ADDRESS from USER where ID in (1,2,3)")
for row in data:
   print("ID号为 ", row[0])
   print("姓名是 ", row[1])
   print("电话是 ", row[2])
   print("公司是 ", row[3])
   print("地址是 ", row[4])

#删除
import sqlite3
conn = sqlite3.connect('D:\\大三下\\github\\作业\\第十次作业 增删改查\\1720350.db')
conn.execute("delete from USER where COMPANY='出租公司'")
conn.commit()
print("删除后，数据更新为:", conn.total_changes)
num2=conn.total_changes
print("{0} rows changed in table USER.".format(num2))

#更改
import sqlite3
conn = sqlite3.connect('D:\\大三下\\github\\作业\\第十次作业 增删改查\\1720350.db')
conn.execute("UPDATE USER set ADDRESS ='阿里巴巴' where ID=3")
conn.commit()
print("更改后，数据更新为", conn.total_changes)
data2 = conn.execute("SELECT ID,NAME,PHONE,COMPANY,ADDRESS from USER where ID=3")
for row in data2:
   print("ID号为 ", row[0])
   print("姓名是 ", row[1])
   print("电话是 ", row[2])
   print("公司是 ", row[3])
   print("地址是 ", row[4])
conn.close()

"""结果是：
数据库已经被成功的打开
数据库表创建成功
3 rows changed in table USER.
已经成功打开数据表
ID号为  1
姓名是  小a
电话是  12345678915
公司是  出租公司
地址是  人民广场
ID号为  2
姓名是  小b
电话是  52663489112
公司是  建桥学院
地址是  滴水湖
ID号为  3
姓名是  小c
电话是  52436125489
公司是  大酒店
地址是  徐家汇
删除后，数据更新为: 1
1 rows changed in table USER.
更改后，数据更新为 1
ID号为  3
姓名是  小c
电话是  52436125489
公司是  大酒店
地址是  阿里巴巴
"""