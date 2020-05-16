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


class Contact:
    def __init__(self, name, tel, com, addr):
        self.name = name
        self.tel = tel
        self.com = com
        self.addr = addr


def create_database_table(connection):
    connection.execute("CREATE TABLE CONTACT(\
    ID INTEGER PRIMARY KEY AUTOINCREMENT,\
    NAME TEXT NOT NULL,\
    TEL TEXT NOT NULL,\
    COM TEXT,\
    ADDR TEXT\
    );")
    print("---Table CONTACT created successfully---")


def new_contact(n, t, c, a):
    return Contact(n, t, c, a)


def get_contact_by_name(connection, name):
    return connection.execute("select * from CONTACT where name = '%s'" % name)


def get_all_contact(connection):
    return connection.execute("select * from CONTACT")


def add_contact(connection, contact):
    connection.execute("insert into CONTACT(name, tel, com, addr) values('%s', '%s', '%s', '%s')" % (
        contact.name, contact.tel, contact.com, contact.addr))
    connection.commit()


def del_contact(connection, name, tel):
    connection.execute("delete from CONTACT where name = '%s' and tel = '%s'" % (name, tel))
    connection.commit()


def main():
    conn = sqlite3.connect('hw10_1720425.db')
    create_database_table(conn)

    contact1 = new_contact("ZhangSan", "12345678901", "SJQU", "No.1111 HuChengHuan Rd")
    contact2 = new_contact("LiSi", "12345678902", "SJQU", "No.1111 HuChengHuan Rd")
    contact3 = new_contact("WangWu", "12345678903", "SJQU", "No.1111 HuChengHuan Rd")
    contact4 = new_contact("ZhaoLiu", "12345678904", "SJQU", "No.1111 HuChengHuan Rd")

    add_contact(conn, contact1)
    add_contact(conn, contact2)
    add_contact(conn, contact3)
    add_contact(conn, contact4)

    cursor1 = get_all_contact(conn)
    print("查询数据库中所有联系人信息：")
    for row in cursor1:
        print(row)
    print("")
    cursor1.close()

    cursor2 = get_contact_by_name(conn, "WangWu")
    print("查询数据库中WangWu的所有信息：")
    for row in cursor2:
        print(row)
    print("")
    cursor2.close()

    del_contact(conn, "ZhaoLiu", "12345678904")
    print("已删除 name='ZhaoLiu', tel='12345678904' 的联系人！")
    print("")

    cursor3 = get_all_contact(conn)
    print("查询数据库中所有联系人信息：")
    for row in cursor3:
        print(row)
    print("")
    cursor3.close()

    conn.close()


main()
