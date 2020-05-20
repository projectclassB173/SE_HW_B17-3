import sqlite3
conn=sqlite3.connect('E:\\sql\\test.db')
print("Opened database successfully");
#conn.execute('CREATE TABLE USER (ID INT PRIMARY KEY NOT NULL ,NAME CHAR NOT NULL ,PHONE CHAR NOT NULL ,COM CHAR NOT NULL ,AD CHAR NOT NULL );')
#print("Table USER created successfully");

n=-1
while n!=0:
    n = int(input("请选择需要使用的功能：\n1.新增联系人\n2.查询联系人\n3.删除联系人\n4.查询所有\n0.退出\n请输入："))
    if n==1:
        conn = sqlite3.connect('E:\\sql\\test.db')
        addid=input("请输入编号：\n")
        addname=input("请输入姓名：\n")
        phone=input("请输入电话：\n")
        com=input("请输入所在公司：\n")
        add=input("请输入地址：\n")
        conn.execute("INSERT INTO USER (ID,NAME,PHONE,COM,AD) VALUES ('"+addid+"','"+addname+"','"+phone+"','"+com+"','"+add+"')")
        conn.commit()
        print("Insert operation successfully.")
    elif n==2:
        conn = sqlite3.connect('E:\\sql\\test.db')
        searchname = input("请输入姓名：\n")
        search=conn.execute("SELECT NAME,PHONE,COM,AD FROM USER WHERE NAME='"+searchname+"'")
        for row in search:
            print("Name=",row[0])
            print("Phone=",row[1])
            print("COM=",row[2])
            print("ADD=",row[3])
        print("Operation done successfully")
    elif n==3:
        conn = sqlite3.connect('E:\\sql\\test.db')
        deletename=input("请输入姓名：\n")
        conn.execute("DELETE FROM USER WHERE NAME='"+deletename+"'")
        conn.commit()
        print("Operation done successfully")
    elif n==4:
        conn = sqlite3.connect('E:\\sql\\test.db')
        findall=conn.execute("SELECT * FROM USER")
        for userlist in findall:
            print(userlist)
    conn.close()


