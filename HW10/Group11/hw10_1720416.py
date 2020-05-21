#编写一个Python程序，采用SQLite数据库实现通讯录管理功能。
#采用SQLite数据库存放个人通讯录，要求存放联系人的姓名、电话、公司、地址；
#设计相应的函数完成以下数据库操作：
#创建数据库表；
#新增联系人；
#按姓名查询联系人详细信息；
#删除联系人；

import sqlite3

conn=sqlite3.connect('D:\\课程\\大三下\\项目实战\\本地数据库\\practice.db')
print("成功打开practice数据库")

conn.execute('CREATE TABLE AddressBook(NAME PRIMARY KEY NOT NULL,TELEPHONE CHAR NOT NULL,COMPANY CHAR NOT NULL,ADDRESS CHAR NOT NULL);')
print("成功创建AddressBook表")

m = int(input("1.新增联系人\n
    2.按姓名查询联系人详细信息\n
    3.删除联系人\n"))
if m==1:
    conn = sqlite3.connect('D:\\课程\\大三下\\项目实战\\本地数据库\\practice.db')
    name = input("请输入联系人姓名：\n")
    telephone = input("请输入联系人电话：\n")
    company = input("请输入联系人公司：\n")
    address = input("请输入联系人地址：\n")
    conn.execute("INSERT INTO AddressBook (NAME,TELEPHONE,COMPANY,ADDRESS) VALUES ('"+ name +"','"+ telephone +"','"+ company +"','"+ address +"')")
    print("成功新增联系人{0}".format(name))
    conn.commit()
elif m==2:
    conn = sqlite3.connect('D:\\课程\\大三下\\项目实战\\本地数据库\\practice.db')
    name = input("请输入要查询的联系人姓名：\n")
    search = conn.execute("SELECT NAME,TELEPHONE,COMPANY,ADDRESS FROM AddressBook WHERE NAME='"+ name +"'")
    for row in search:
        print("联系人姓名：",row[0])
        print("联系人电话：",row[1])
        print("联系人公司：",row[2])
        print("联系人地址：",row[3])
    conn.commit()
elif m==3:
    conn = sqlite3.connect('D:\\课程\\大三下\\项目实战\\本地数据库\\practice.db')
    name = input("请输入要删除的联系人姓名：\n")
    conn.execute("DELETE FROM AddressBook WHERE NAME='"+ name +"'")
    print("成功删除联系人{0}".format(name))
    conn.commit()
else:
    print("输入的内容有误，请输入123中的任意数字")
conn.close()


>>>
============== RESTART: D:\课程\大三下\项目实战\课后作业\Python\hw10_1720416.py =============
成功打开practice数据库
请选择需要使用的功能：
1.新增联系人
2.按姓名查询联系人详细信息
3.删除联系人
1
请输入联系人姓名：
xxy
请输入联系人电话：
1720416
请输入联系人公司：
shanghai
请输入联系人地址：
shanghai
成功新增联系人xxy
>>>
============== RESTART: D:\课程\大三下\项目实战\课后作业\Python\hw10_1720416.py =============
成功打开practice数据库
请选择需要使用的功能：
1.新增联系人
2.按姓名查询联系人详细信息
3.删除联系人
2
请输入要查询的联系人姓名：
xxy
联系人姓名： xxy
联系人电话： 1720416
联系人公司： shanghai
联系人地址： shanghai
>>>
============== RESTART: D:\课程\大三下\项目实战\课后作业\Python\hw10_1720416.py =============
成功打开practice数据库
请选择需要使用的功能：
1.新增联系人
2.按姓名查询联系人详细信息
3.删除联系人
3
请输入要删除的联系人姓名：
xxy
成功删除联系人xxy
>>>
============== RESTART: D:\课程\大三下\项目实战\课后作业\Python\hw10_1720416.py =============
成功打开practice数据库
请选择需要使用的功能：
1.新增联系人
2.按姓名查询联系人详细信息
3.删除联系人
4
输入的内容有误，请输入123中的任意数字
>>>
