#编写一个Python程序，采用SQLite数据库实现通讯录管理功能。
#采用SQLite数据库存放个人通讯录，要求存放联系人的姓名、电话、公司、地址；
#设计相应的函数完成以下数据库操作：
##创建数据库表；
##新增联系人；
##按姓名查询联系人详细信息；
##删除联系人；
import sqlite3
def create_database():
    conn = sqlite3.connect('hw10_1720359.db')
    print("Opened database successfully");
    conn.execute('''CREATE TABLE CONTACTS
    (ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME TEXT NOT NULL,
    TELPHONE TEXT NOT NULL,
    COMPANY TEXT NOT NULL,
    ADRESS TEXT NOT NULL);''')
    print("Table contacts created successfully");
    conn.close()
def add_con(name,tel,com,ads):
    conn = sqlite3.connect('hw10_1720359.db')
    print("Opened database successfully")
    conn.execute("INSERT INTO CONTACTS (NAME,TELPHONE,COMPANY,ADRESS) VALUES ('"+name+"', '"+tel+"', '"+com+"', '"+ads+"')")
    conn.commit()
    num1=conn.total_changes
    print("{0} rows changed in table contacts.".format(num1))
    print("Insert operation successfully.")
    conn.close()
def search_byname(name):
    conn = sqlite3.connect('hw10_1720359.db')
    cursor1 = conn.execute("SELECT ID,NAME,TELPHONE,COMPANY,ADRESS from CONTACTS where NAME ='"+name+"'")
    for row in cursor1:
        print("ID = ", row[0],end=' ')
        print("NAME = ", row[1],end=' ')
        print("TELPHONE = ", row[2],end=' ')
        print("COMPANY = ", row[3],end=' ')
        print("ADRESS = ", row[4])
        conn.close()
print("Operation done successfully")
def del_byname(name):
    conn = sqlite3.connect('hw10_1720359.db')
    cursor1 = conn.execute("delete from CONTACTS where NAME ='"+name+"'")
    num1=conn.total_changes
    print("{0} rows changed in table CONTACTS.".format(num1))
    print("Contact "+name+" delete successfully")
    conn.close()





if __name__=="__main__":
    create_database()
    flag='1'
    while flag=='1':
        i=input("1.新建联系人\n2.查找联系人\n3.删除联系人\n4.退出系统\n请输入：")
        if i=='1':             
            name=input("请输入姓名：")
            tel=input("请输入电话：")
            com=input("请输入公司：")
            ads=input("请输入地址：")
            add_con(name,tel,com,ads)
        elif i=='2':  
            search_byname(input("请输入查找的联系人姓名："))
        elif i=='3':
            del_byname(input("请输入删除的联系人姓名："))
        else : flag='-1'
    
