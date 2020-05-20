'''
��дһ��Python���򣬲���SQLite���ݿ�ʵ��ͨѶ¼�����ܡ�
����SQLite���ݿ��Ÿ���ͨѶ¼��Ҫ������ϵ�˵��������绰����˾����ַ��
�����Ӧ�ĺ�������������ݿ������
    �������ݿ��
    ������ϵ�ˣ�
    ��������ѯ��ϵ����ϸ��Ϣ��
    ɾ����ϵ�ˣ�
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

    contact1 = new_contact("zhang", "1854968548", "tet", "No.0001 garden")
    contact2 = new_contact("li", "12345678902", "al", "No.0002 road")
    contact3 = new_contact("wang", "15896354125", "mad", "No.0003 jiangsu")
    contact4 = new_contact("zhao", "18695485632", "cao", "No.0004 hubei")

    add_contact(conn, contact1)
    add_contact(conn, contact2)
    add_contact(conn, contact3)
    add_contact(conn, contact4)

    cursor1 = get_all_contact(conn)
    print("��ѯ���ݿ���������Ϣ��")
    for row in cursor1:
        print(row)
    print("")
    cursor1.close()

    cursor2 = get_contact_by_name(conn, "wang")
    print("��ѯ���ݿ���wang����Ϣ��")
    for row in cursor2:
        print(row)
    print("")
    cursor2.close()

    del_contact(conn, "zhao", "18695485632")
    print("��ɾ��")
    print("")

    cursor3 = get_all_contact(conn)
    print("��ѯ���ݿ���������ϵ����Ϣ��")
    for row in cursor3:
        print(row)
    print("")
    cursor3.close()

    conn.close()


main()
