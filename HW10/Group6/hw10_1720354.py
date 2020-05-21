# 编写一个Python程序，采用SQLite数据库实现通讯录管理功能。
# 采用SQLite数据库存放个人通讯录，要求存放联系人的姓名、电话、公司、地址；
# 设计相应的函数完成以下数据库操作：
# 创建数据库表；
# 新增联系人；
# 按姓名查询联系人详细信息；
# 删除联系人；


import sqlite3


def create_table():#创建表
    conn = sqlite3.connect('per_contact.db')
    cursor = conn.cursor()
    try:
        cursor.execute("create table t_contact(id integer primary key not null,name text not null,phone text not null,company text not null,addd text not null);")
        conn.commit()
        print('t_contact表创建成功')
    except:
        print('t_contact表创建失败，请检查是否出现了问题')
    finally:
        cursor.close()
        conn.close()


def add_data():#添加通讯录用户数据
    conn = sqlite3.connect('per_contact.db')
    cursor = conn.cursor()
    print('数据库连接成功')
    id = int(input('请输入id：'))
    name = input('请输入姓名：')
    phone = input('请输入电话：')
    company = input('请输入公司:')
    addd = input('请输入地址:')
    try:#sql语句插入
        sqlSentence = 'insert into t_contact(id,name,phone,company,addd)'
        sqlSentence += 'values("%d","%s","%s","%s","%s")' % (id, name, phone, company, addd)
        conn.execute(sqlSentence)
        conn.commit()
        print("恭喜，您成功的插入了数据")
    except:
        print('不好意思，您的数据插入失败，请检查是否有出现问题')
    finally:
        cursor.close()
        conn.close()


def search_data():#查询通讯录数据
    conn = sqlite3.connect('per_contact.db')
    cursor = conn.cursor()
    print('数据库连接成功')
    se_name = input('请输入要查询的名字')
    sqlSentence2 = "select id,name,phone,company,addd from t_contact where name like '%" + se_name + "%'"
    result = cursor.execute(sqlSentence2)
    re_result = result.fetchall()
    if len(re_result) != 0:#循环输出结果
        for row in re_result:
            print("id:{0}".format(row[0]))
            print("姓名:{0}".format(row[1]))
            print("电话:{0}".format(row[2]))
            print("公司:{0}".format(row[3]))
            print("地址:{0}".format(row[4]))
    else:
        print("没有查询到这个用户")
    cursor.close()
    conn.close()


def del_data():#删除通讯录用户数据
    conn = sqlite3.connect('per_contact.db')
    cursor = conn.cursor()
    print('数据库连接成功')
    de_name = input('请输入要删除的名字')
    sqlSentence2 = "delete from t_contact where name='%s'" % de_name
    conn.execute(sqlSentence2)
    conn.commit()
    print("删除成功")
    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_table()
    add_data()
    search_data()
    del_data()

