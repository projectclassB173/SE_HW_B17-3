import sqlite3
class User:
    def __init__(self,name,telphone,firm,addr):
        self.name=name
        self.telphone=telphone
        self.firm=firm
        self.addr=addr

#创建表user,记录联系信息
def create_tb(conn):
    sql="create table user" \
        "(id int PRIMARY KEY,name text NOT NULL ,telphone text,firm text,addr text);"
    conn.execute(sql)
    conn.commit()
    print('数据库表创建成功')

#添加联系人信息
def add(conn,user):
    sql="insert into user(name,telphone,firm,addr) values('%s','%s','%s','%s')" %\
        (user.name,user.telphone,user.firm,user.addr)
    conn.execute(sql)
    conn.commit()
    print("{}的个人信息添加成功！".format(user.name))

#根据姓名查找联系人
def queryByName(conn,name):
    sql="select * from user where name='%s'" % (name)
    cur=conn.execute(sql)
    print('{}的联系信息：'.format(name))
    for row in cur:
        print(row)
    cur.close()

#根据姓名删除联系人
def delByName(conn,name):
    sql="delete from user where name='%s'" % (name)
    conn.execute(sql)
    conn.commit()
    print("删除{}成功！".format(name))

def main():
    conn=sqlite3.connect("user_info.db")
    create_tb(conn)

    user1=User('norton','15215474586','亚马逊','霍格沃兹格兰芬多')
    user2=User('jack','17765897858','谷歌','霍格沃兹赫奇帕奇')
    user3=User('rose','15245698756','阿里巴巴','霍格沃兹拉文克劳')
    user4=User('hali','14789654235','腾讯','霍格沃兹斯莱特林')
    add(conn,user1)
    add(conn,user2)
    add(conn,user3)
    add(conn,user4)

    queryByName(conn,'norton')

    queryByName(conn,'jack')

    delByName(conn,'norton')
if __name__ == '__main__':
    main()
