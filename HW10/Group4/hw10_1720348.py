import sqlite3


class connect:
    def __init__(self):        # 初始化数据库连接，初始化游标
        self.conn = sqlite3.connect("connect.db")
        self.c = self.conn.cursor()

    def close(self):   # 关闭数据库操作
        self.c.close()
        self.conn.close()

    def create_table(self):  # 创建表，如果数据库中已经存在，则抛出异常
        try:
            self.c.execute('''CREATE TABLE t_adb
                (id INTEGER PRIMARY KEY NOT NULL,
                name TEXT NOT NULL,
                phone TEXT NOT NULL ,
                company TEXT,
                address TEXT);''')
            self.conn.commit()
            print("表顺利创建\n")
        except sqlite3.OperationalError as reason:
            print("创建失败， " + str(reason) + "\n")

    @staticmethod
    def init_data():    # 获取用户需要插入的数据，返回值为一个列表
        try:
            Id = input("ID:") or None
            name = input("姓名:") or None
            phone = input("电话:") or None
            company = input("公司:") or None
            address = input("地址:") or None
            init = [Id, name, phone, company, address]
            return init
        except ValueError as reason:
            print("警告" + str(reason))

    def add_contacts(self, init):  # 传入之前用户输入的内容
        try:
            self.c.execute("INSERT INTO t_adb VALUES(?,?,?,?,?)",
                           (init[0], init[1], init[2], init[3], init[4]))
            self.conn.commit()
            print("INFO: Affected Rows 1\n")
        except sqlite3.IntegrityError as reason:
            print("警告: " + str(reason) + "\n")
        except TypeError as reason:
            print("警告: " + str(reason) + "\n")
        except sqlite3.OperationalError as reason:
            print("警告: " + str(reason))
            print("请先创建表.\n")

    @staticmethod
    def input_name():
        name = input("请输入姓名:")
        return name

    def find_by_name(self, name):
        try:
            result = self.c.execute("SELECT * FROM t_adb WHERE name='{}'".format(name))
            if result:
                for each in result:
                    print("ID:{} 姓名:{} 电话:{} 公司:{} 地址:{}\n"
                          .format(each[0], each[1], each[2], each[3], each[4]))
            else:
                print("INFO: {} is not in t_adb\n".format(name))
        except sqlite3.OperationalError as reason:
            print("警告: " + str(reason))
            print("请先创建表.\n")

    def delete_by_name(self, name):
        try:
            self.c.execute("DELETE FROM t_adb WHERE name='{}'".format(name))
            self.conn.commit()
            print("INFO: Affected Rows 1\n")
        except sqlite3.OperationalError as reason:
            print("警告: " + str(reason))
            print("请先创建表.\n")

    @staticmethod
    def show_menu():
        print("-      XX通讯录       -")
        print("-      1.创建表       -")
        print("-      2.新增联系人    -")
        print("-      3.按姓名查询    -")
        print("-      4.删除联系人    -")
        print("-      0.退出系统      -")

    def main(self):  # 通讯录的主函数
        while True:
            self.show_menu()
            try:    # try判断用户的输入是否合法，过滤非数字字符
                opt = int(input("你的操作:"))
            except ValueError:
                print("WARNING: Illegal string\n")
                continue
            if opt == 0:
                print("退出系统.")
                return
            elif opt == 1:
                self.create_table()
            elif opt == 2:
                self.add_contacts(self.init_data())
            elif opt == 3:
                self.find_by_name(self.input_name())
            elif opt == 4:
                self.delete_by_name(self.input_name())
            else:
                print("无此操作,请重新选择...\n")


if __name__ == "__main__":
    con = connect()
    con.main()
    con.close()