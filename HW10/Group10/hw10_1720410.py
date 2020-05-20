#编写一个Python程序，采用SQLite数据库实现通讯录管理功能。
#采用SQLite数据库存放个人通讯录，要求存放联系人的姓名、电话、公司、地址；
#设计相应的函数完成以下数据库操作：
#创建数据库表；
#新增联系人；
#按姓名查询联系人详细信息；
#删除联系人；
import sqlite3
class ConnDB:
    def __init__(self):
        self.conn = sqlite3.connect("hyc.db")
        self.sql = self.conn.cursor()

        while True:
            print('1.新建表')
            print('2.新增联系人')
            print('3.删除联系人')
            print('4.查询联系人')
            print('5.退出程序')
            x = input("请输入您的选择:")
            if x == '1':
                self.__create_table()
                continue
            elif x == '2':
                self.__add_contacts(self.__init_data())
                continue
            elif x == '3':
                self.__delete_name(self.__input_name())
                continue
            elif x == '4':
                self.__find_name(self.__input_name())
                continue
            elif x == '5':
                print("成功退出！")
                exit()
                continue

    def close(self):
        self.sql.close()
        self.conn.close()

    def __create_table(self):
        try:
            self.sql.execute('''CREATE TABLE abc
                (id INTEGER NOT NULL PRIMARY KEY,
                name TEXT NOT NULL,
                number TEXT NOT NULL ,
                company TEXT NULL ,
                address TEXT NULL);''')
            self.conn.commit()
            print("成功新建表！")
        except:
           pass

    # 增加用户信息
    def __init_data(self):
        try:
            id = input('请输入id:')
            name = input('请输入姓名：')
            number = input('请输入电话:')
            company = input('请输入公司:')
            address = input('请输入地址:')
            init = [id, name, number, company, address]
            return init
        except:
            pass

    def __add_contacts(self, init):
        try:
            self.sql.execute("INSERT INTO abc(id, name, number, company, address) VALUES(?,?,?,?,?)", \
                             (init[0], init[1], init[2], init[3], init[4]))
            self.conn.commit()
            print("添加信息成功！")
        except:
            pass


    # 删除用户信息
    def __delete_name(self, name):
        try:
            self.sql.execute("DELETE FROM abc WHERE name='%s'" % name)
            self.conn.commit()
            print("删除信息成功!")
        except:
            pass


  # 查询用户信息
    def __input_name(self):
        name = input("请输入姓名:")
        return name
    def __find_name(self, name):
        try:
            result = self.sql.execute("SELECT * FROM abc WHERE name LIKE '%"+name+"%'")
            if result:
                for each in result:
                    print("id:%d name:%s number:%s company:%s address:%s" % (each[0], each[1], each[2], each[3], each[4]))
            else:
                print("该用户不存在！")
        except:
            pass

if __name__ == "__main__":
    connect = ConnDB()
    connect.close()
'''
    "D:\program files\python\venv\Scripts\python.exe" "D:/program files/python/hw10_1720410.py"
    1.
    新建表
    2.
    新增联系人
    3.
    删除联系人
    4.
    查询联系人
    5.
    退出程序
    请输入您的选择: 1
    成功新建表！
    1.
    新建表
    2.
    新增联系人
    3.
    删除联系人
    4.
    查询联系人
    5.
    退出程序
    请输入您的选择: 2
    请输入id: 1
    请输入姓名：黄钰晨
    请输入电话: 273784848
    请输入公司: sdddhj
    请输入地址: qfdweyf
    添加信息成功！
    1.
    新建表
    2.
    新增联系人
    3.
    删除联系人
    4.
    查询联系人
    5.
    退出程序
    请输入您的选择: 4
    请输入姓名: 黄钰晨
    id: 1
    name: 黄钰晨
    number: 273784848
    company: sdddhj
    address: qfdweyf
    1.
    新建表
    2.
    新增联系人
    3.
    删除联系人
    4.
    查询联系人
    5.
    退出程序
    请输入您的选择: 3
    请输入姓名: 黄钰晨
    删除信息成功!
    1.
    新建表
    2.
    新增联系人
    3.
    删除联系人
    4.
    查询联系人
    5.
    退出程序
    请输入您的选择: 5
    成功退出！
'''