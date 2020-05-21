'''编写一个Python程序，采用SQLite数据库实现通讯录管理功能。
v采用SQLite数据库存放个人通讯录，要求存放联系人的姓名、电话、公司、地址；
v设计相应的函数完成以下数据库操作：
n创建数据库表；
n新增联系人；
n按姓名查询联系人详细信息；
n删除联系人； '''
import sqlite3


class Addresslook:
    def __init__(self):
        self.conn = sqlite3.connect('D:\python\陈声盛\Addresslook.db')
        print("Opened database successfully")


    def create_table(self):
            self.conn.execute('''CREATE TABLE Addresslook
            (ID INT PRIMARY KEY     NOT NULL,
            NAME            TEXT    NOT NULL,
            TELEPHONE       TEXT    NOT NULL,
            CORPORATION         TEXT,
            ADDRESS         TEXT);''')
    print("Table Addresslook created successfully")


    def insert(self,id='null',name='null',phone='null',corporation='null',adress='null'):
        self.conn.execute("INSERT INTO Addresslook (ID,NAME,TELEPHONE, CORPORATION,ADDRESS) \
        VALUES('%d', '%s', '%s', '%s', '%s')" % (id, name, phone, corporation, adress))
        self.conn.commit()
        print("insert successfully！")


    def search_by_name(self,name):
        cursor1 = self.conn.execute("SELECT * from Addresslook where NAME = '%s'" % (name))
        for row in cursor1:
            print("ID = ", row[0])
            print("NAME = ", row[1])
            print("TELEPHONE = ", row[2])
            print("CORPORATION = ", row[3])
            print("ADDRESS = ", row[4])
            print("query successfully！")



    def delete(self,id):
        self.conn.execute("delete from Addresslook where ID = '%s'" % (id))
        self.conn.commit()
        print("delete successfully")


    def select_all(self):
        cursor2 = self.conn.execute("SELECT * from Addresslook")
        for row in cursor2:
            print("ID = ", row[0])
            print("NAME = ", row[1])
            print("TELEPHONE = ", row[2])
            print("CORPORATION = ", row[3])
            print("ADDRESS = ", row[4])
            print("Operation done successfully")


main=Addresslook()

main.create_table()
main.insert(1,'陈声盛','1358745125','2587415','上海')
main.insert(2,'张三','12345678910','98770526','重庆')

main.select_all()
main.search_by_name('陈声盛')
main.delete(2)

main.select_all()


#结果
'''
Table Addresslook created successfully

Opened database successfully

insert successfully！
insert successfully！

ID =  1
NAME =  陈声盛
TELEPHONE =  1358745125
COMPANY =  2587415
ADDRESS =  上海
Operation done successfully
ID =  2
NAME =  张三
TELEPHONE =  12345678910
COMPANY =  98770526
ADDRESS =  重庆
Operation done successfully

ID =  1
NAME =  陈声盛
TELEPHONE =  1358745125
COMPANY =  2587415
ADDRESS =  上海
query successfully！

delete successfully

ID =  1
NAME =  陈声盛
TELEPHONE =  1358745125
COMPANY =  2587415
ADDRESS =  上海
Operation done successfully


'''
