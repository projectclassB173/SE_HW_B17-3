"""
Asahi Huang
2020.05.21
 """

import sqlite3
from person import Person


# 创建数据库
def conn_db():
    conn = sqlite3.connect('address_book.db')
    conn.execute(
        "create table t_person( ID INT primary key, name text not null,\
       telephone text,company text,address text )")
    print("Table t_person created successful")
    conn.commit()
    conn.close()


# 添加联系人
def addPerson():
    conn = sqlite3.connect("address_book.db")
    id = int(input("Input id: "))
    name = input("Input name: ")
    telephone = input("Input telephone: ")
    company = input("Input company: ")
    address = input("Input address: ")
    person = Person(id, name, telephone, company, address)
    conn.execute("insert into t_person (id,name,telephone,company,address) \
  values('%d','%s','%s','%s','%s')" % (person.id, person.name, person.telephone, person.company, person.address))
    print("Add %s sucessfully" % person.name)
    conn.commit()
    conn.close()

# 按姓名查询


def findByName(name):
    conn = sqlite3.connect("address_book.db")
    person = conn.execute("SELECT id,name,telephone,company,address \
         FROM t_person WHERE name = '%s'" % (name))

    for row in person:
        print("Id: ", row[0])
        print("Name: ", row[1])
        print("Telephone: ", row[2])
        print("Company: ", row[3])
        print("Address: ", row[4])
    conn.close()


def deleteById(id):
    conn = sqlite3.connect("address_book.db")
    conn.execute("DELETE FROM t_person WHERE ID = %d" % (id))
    print("Delete successfully")
    conn.commit()
    conn.close()


if __name__ == '__main__':
    while True:
        print(5*"=", "通讯录管理系统:", 5*"=")
        print("1. 创建通讯录表")
        print("2. 新增联系人")
        print("3. 按姓名查询联系人详细信息")
        print("4. 删除联系人")
        print("5. 退出")
        n = int(input("输入选项序号："))
        if n == 5:
            print("再见")
            break
        elif n == 1:
            conn_db()
        elif n == 2:
            addPerson()
        elif n == 3:
            name = input("输入要查询的名字:")
            findByName(name)
        elif n == 4:
            id = int(input("输入要删除的联系人id:"))
            deleteById(id)
        else:
            print("输入1-5的数字")
