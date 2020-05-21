#1910008顾俊
# 编写一个Python程序，采用SQLite数据库实现通讯录管理功能。
# 采用SQLite数据库存放个人通讯录，要求存放联系人的姓名、电话、公司、地址；
# 设计相应的函数完成以下数据库操作：
# 创建数据库表；
# 新增联系人；
# 按姓名查询联系人详细信息；
# 删除联系人；


import sqlite3


def create_table():
    conn = sqlite3.connect('per_comm.db')
    cursor = conn.cursor()
    try:
        cursor.execute("create table t_comm(id integer primary key not null,name text not null,tel text not null,company text not null,addr text not null);")
        conn.commit()
        print('t_comm表创建成功')
        print('gj--------------------------------------------')
    except:
        print('t_comm表创建失败')
        print('gj--------------------------------------------')
    finally:
        cursor.close()
        conn.close()


def add_data():
    conn = sqlite3.connect('per_comm.db')
    cursor = conn.cursor()
    print('数据库连接成功')
    ID = int(input('请输入id：'))
    name = input('请输入姓名：')
    tel = input('请输入电话：')
    company = input('请输入公司:')
    Addr = input('请输入地址:')
    try:
        sql_one = 'insert into t_comm(id,name,tel,company,Addr)'
        sql_one += 'values("%d","%s","%s","%s","%s")' % (ID, name, tel, company, Addr)
        conn.execute(sql_one)
        conn.commit()
        print("插入数据成功！！")
        print('gj--------------------------------------------')
    except:
        print('插入数据失败！！')
        print('gj--------------------------------------------')
    finally:
        cursor.close()
        conn.close()


def search_data():
    conn = sqlite3.connect('per_comm.db')
    cursor = conn.cursor()
    print('数据库连接成功')
    se_name = input('请输入要查询的名字')
    sql_two = "select id,name,tel,company,addr from t_comm where name like '%" + se_name + "%'"
    result = cursor.execute(sql_two)
    re_result = result.fetchall()
    if len(re_result) != 0:
        for row in re_result:
            print("id:{0}".format(row[0]))
            print("姓名:{0}".format(row[1]))
            print("电话:{0}".format(row[2]))
            print("公司:{0}".format(row[3]))
            print("地址:{0}".format(row[4]))
            print('gj--------------------------------------------')
    else:
        print("查无此人")
        print('gj--------------------------------------------')
    cursor.close()
    conn.close()


def del_data():
    conn = sqlite3.connect('per_comm.db')
    cursor = conn.cursor()
    print('数据库连接成功')
    de_name = input('请输入要删除的名字')
    sql_three = "delete from t_comm where name='%s'" % de_name
    conn.execute(sql_three)
    conn.commit()
    print("删除成功")
    cursor.close()
    conn.close()


create_table()
add_data()
search_data()
del_data()






'''
gj--------------------------------------------
数据库连接成功
请输入id：7
请输入姓名：顾俊
请输入电话：123456
请输入公司:111company
请输入地址:2road
插入数据成功！！
gj--------------------------------------------
数据库连接成功
请输入要查询的名字d
id:5
姓名:d
电话:dd
公司:dddd
地址:dddddd
gj--------------------------------------------
数据库连接成功
请输入要删除的名字d
删除成功
'''




