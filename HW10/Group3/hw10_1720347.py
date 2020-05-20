#编写一个Python程序，采用SQLite数据库实现通讯录管理功能。
#v采用SQLite数据库存放个人通讯录，要求存放联系人的姓名、电话、公司、地址；
#v设计相应的函数完成以下数据库操作：
#n创建数据库表；
#n新增联系人；
#n按姓名查询联系人详细信息；
#n删除联系人；
import sqlite3


class AddressList:
    def __init__(self):
        self.conn = sqlite3.connect('C:\\testsql\\addresslist.db')
        print("Opened database successfully");

    def shutdown(self):
        self.conn.close()
        print('Database connection has been shutdown')

    def create_table(self):
        self.conn.execute('''CREATE TABLE USER
        (ID INT PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,
        TEL CHAR(50) NOT NULL,
        COMPANY CHAR(50),
        ADDRESS CHAR(50));''')
        print("Table USER created successfully");

    def insert_line(self):
        uid = input("ID:")
        name = input("Name:")
        tel = input("Tel:")
        company = input("Company:")
        address = input("Address:")
        lines = [uid, name, tel, company, address]
        self.conn.execute("INSERT INTO USER (ID,NAME,TEL,COMPANY,ADDRESS) \
        VALUES(?,?,?,?,?)", (lines[0], lines[1], lines[2], lines[3], lines[4]))
        self.conn.commit()
        num1 = self.conn.total_changes
        print("{0} rows changed in table USER.".format(num1))

    def search_by_name(self):
        name = input('请输入要查询的用户姓名')
        cursor1 = self.conn.execute("SELECT ID,NAME,TEL,COMPANY,ADDRESS from USER where Name = '%s'" % name)
        for row in cursor1:
            print("ID = ", row[0])
            print("NAME = ", row[1])
            print("TEL = ", row[2])
            print("COMPANY = ", row[3])
            print("ADDRESS = ", row[4])
        print("SearchByName Operation done successfully")
        cursor1.close()

    def delete_table(self):
        name = input("请输入所要删除的联系人姓名:")
        self.conn.execute("delete from USER where name='%s'" % name)
        self.conn.commit()
        print("Delete Operation done successfully")

    def menu(self):
        print('1.新增联系人')
        print('2.姓名查询联系人')
        print('3.删除联系人')
        print('4.创建通讯表')
        print('5.退出程序')
        print('请选择功能')

    def main(self):
        #self.create_table()
        self.menu()
        x = input('请输入您的选择菜单号:')
        if x == '1':
            self.insert_line()
        elif x == '2':
            self.search_by_name()
        elif x == '3':
            self.delete_table()
        elif x == '4':
            self.create_table()
        elif x == '5':
            self.shutdown()
        else:
            print("input error！")


if __name__ == "__main__":
    al = AddressList()
    al.main()






