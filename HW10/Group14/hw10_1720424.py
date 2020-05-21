#编写一个Python程序，采用SQLite数据库实现通讯录管理功能。
#采用SQLite数据库存放个人通讯录，要求存放联系人的姓名、电话、公司、地址；
#设计相应的函数完成以下数据库操作：
#创建数据库表；
#新增联系人；
#按姓名查询联系人详细信息；
#删除联系人；

import sqlite3
#新建一个数据库
def create_sql():
    sql = sqlite3.connect("user_data.db")
    sql.execute("""create table if not exists
        %s(
        %s integer primary key autoincrement,
        %s varchar(128),
        %s varchar(128),
        %s varchar(128),
        %s char(128))"""
        % ('user',
             'ID',
             'Name',
             'Company',
             'tel',
             'Address'
           ))
    sql.close()
create_sql()
#添加联系人
 def __init_data(self):
        try:
            Id = input("ID:")
            name = input("Name:")
            phone = input("tel:")
            company = input("Company(Optional):")
            address = input("Address(Optional):")
            init = [Id, name, phone, company, address]
            return init
        except:
            pass

    def __add_contacts(self, init): 
        try:
            self.sql.execute("INSERT INTO list(id, name, tel, company, address) VALUES(?,?,?,?,?)", (init[0], init[1], init[2], init[3], init[4]))
            self.conn.commit()
            print("Added")
        except:
            pass

    def __input_name(self):
        name = input("Please input name:")
        return name
#查找
    def __find_name(self, name):
        try:
            result = self.sql.execute("SELECT * FROM list WHERE name LIKE '%"+name+"%'")
            if result:
                for each in result:
                    print("ID:%d Name:%s Tel:%s Company:%s Address:%s" % (each[0], each[1], each[2], each[3], each[4]))
            else:
                print("Not Exist.")
        except:
            pass
#删除（name）
    def __delete_name(self, name):
        try:
            self.sql.execute("DELETE FROM list WHERE name='%s'" % (name))
            self.conn.commit()
            print("Deleted")
        except:
            pass


if __name__ == "__main__":
    connect = ConnDB()
    connect.close()