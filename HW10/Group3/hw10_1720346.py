#编写一个Python程序，采用SQLite数据库实现通讯录管理功能。
#v采用SQLite数据库存放个人通讯录，要求存放联系人的姓名、电话、公司、地址；
#v设计相应的函数完成以下数据库操作：
#n创建数据库表；
#n新增联系人；
#n按姓名查询联系人详细信息；
#n删除联系人；

def create_table(conn):
    conn.execute('''CREATE TABLE CONVT
    (ID INT PRIMARY KEY     NOT NULL, 
    NAME           TEXT    NOT NULL,  
    TELEPHONE      CHAR(15) NOT NULL,
    COMPANY        TEXT    NOT NULL,
    ADDRESS        TEXT    NOT NULL);''')
    conn.commit()

    print('数据库表创建成功')


def add_contact(name, tel, comp, ads, conn):
    conn.execute("INSERT INTO CONVT (NAME,TELPHONE,COMPANY,ADRESS) VALUES ('" +
                 name+"', '"+tel+"', '"+comp+"', '"+ads+"')")
    conn.commit()
    num1 = conn.total_changes
    print("Insert operation successfully.")


def queryname(conn, name):
    sql = "select * from CONVT where name='%s'" % (name)
    cur = conn.execute(sql)
    print('{}的联系信息：'.format(name))
    for row in cur:
        print(row)
    cur.close()


def delt(conn, name):
    cursor1 = conn.execute("delete from CONVT where NAME ='"+name+"'")
    num1 = conn.total_changes
    print("Contact "+name+" delete successfully")


def main():
    conn = sqlite3.connect("fky.db")
    create_table(conn)
    add_contact('fky', '132134212', 'A公司', '地址1', conn)
    add_contact('张三', '654325456', 'B公司', '地址2', conn)
    add_contact('李四', '234343212', 'C公司', '地址3', conn)
    add_contact('王五', '234516765', 'D公司', '地址4', conn)
    queryname(conn, 'fky')
    delt(conn, 'fky')


if __name__ == '__main__':
    main()
