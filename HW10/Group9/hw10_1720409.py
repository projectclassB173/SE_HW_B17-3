'''编写一个Python程序，采用SQLite数据库实现通讯录管理功能。
v采用SQLite数据库存放个人通讯录，要求存放联系人的姓名、电话、公司、地址；
v设计相应的函数完成以下数据库操作：
n创建数据库表；
n新增联系人；
n按姓名查询联系人详细信息；
n删除联系人； '''
import sqlite3




class Telephone:
    def __init__(self):
        self.conn = sqlite3.connect('E:\python\\telephone.db')
        print("Opened database successfully")
        print("----------------------------------------------------------------")

    def create_table(self):
        self.conn.execute('''CREATE TABLE Telephone
            (ID INT PRIMARY KEY     NOT NULL,
            NAME            TEXT    NOT NULL,
            TELEPHONE       TEXT    NOT NULL,
            COMPANY         TEXT,
            ADDRESS         TEXT);''')

    print("Table Telephone created successfully")
    print("----------------------------------------------------------------")

    def insert(self, id='null', name='null', phone='null', company='null', adress='null'):
        self.conn.execute("INSERT INTO Telephone (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
        VALUES('%d', '%s', '%s', '%s', '%s')" % (id, name, phone, company, adress))
        self.conn.commit()
        print("insert successfully！")
        print("----------------------------------------------------------------")

    def search_by_name(self, name):
        cursor1 = self.conn.execute("SELECT * from Telephone where NAME = '%s'" % (name))
        for row in cursor1:
            print("ID = ", row[0])
            print("NAME = ", row[1])
            print("TELEPHONE = ", row[2])
            print("COMPANY = ", row[3])
            print("ADDRESS = ", row[4])
            print("query successfully！")
            print("----------------------------------------------------------------")

    def delete(self, id):
        self.conn.execute("delete from Telephone where ID = '%s'" % (id))
        self.conn.commit()
        print("delete successfully")
        print("----------------------------------------------------------------")

    def select_all(self):
        cursor2 = self.conn.execute("SELECT * from Telephone")
        for row in cursor2:
            print("ID = ", row[0])
            print("NAME = ", row[1])
            print("TELEPHONE = ", row[2])
            print("COMPANY = ", row[3])
            print("ADDRESS = ", row[4])
            print("Operation done successfully")
            print("----------------------------------------------------------------")


test = Telephone()

test.create_table()
test.insert(1, '李唯唯', '18621085092', '84880526', '苏州')
test.insert(2, '王俊凯', '12345678910', '98770526', '重庆')
test.insert(3, '潇潇', '1325478965', '95214426', '北京')
test.select_all()
test.search_by_name('李唯唯')
test.delete(3)

test.select_all()

# 结果
'''
Opened database successfully
----------------------------------------------------------------
Table Telephone created successfully
----------------------------------------------------------------
insert successfully！
----------------------------------------------------------------
insert successfully！
----------------------------------------------------------------
insert successfully！
----------------------------------------------------------------
ID =  1
NAME =  李唯唯
TELEPHONE =  18621085092
COMPANY =  84880526
ADDRESS =  苏州
Operation done successfully
----------------------------------------------------------------
ID =  2
NAME =  王俊凯
TELEPHONE =  12345678910
COMPANY =  98770526
ADDRESS =  重庆
Operation done successfully
----------------------------------------------------------------
ID =  3
NAME =  潇潇
TELEPHONE =  1325478965
COMPANY =  95214426
ADDRESS =  北京
Operation done successfully
----------------------------------------------------------------
ID =  1
NAME =  李唯唯
TELEPHONE =  18621085092
COMPANY =  84880526
ADDRESS =  苏州
query successfully！
----------------------------------------------------------------
delete successfully
----------------------------------------------------------------
ID =  1
NAME =  李唯唯
TELEPHONE =  18621085092
COMPANY =  84880526
ADDRESS =  苏州
Operation done successfully
----------------------------------------------------------------
ID =  2
NAME =  王俊凯
TELEPHONE =  12345678910
COMPANY =  98770526
ADDRESS =  重庆
Operation done successfully
----------------------------------------------------------------


'''
