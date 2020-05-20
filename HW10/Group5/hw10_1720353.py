import sqlite3
class ConnDB:
    def __init__(self):    
        self.conn = sqlite.connect("address_list.db")
        self.c = self.conn.cursor()

    def close(self): 
        self.c.close()
        self.conn.close()

    def create_table(self):  
        try:
            self.c.execute('''CREATE TABLE t_adb
                (id INTEGER PRIMARY KEY NOT NULL,
                name TEXT NOT NULL,
                phone TEXT NOT NULL ,
                company TEXT,
                address TEXT);''')
            self.conn.commit()
            print("t_adb was successfully created!\n")
        except sqlite.OperationalError as reason:
            print("WARNING: t_adb could not be created because " + str(reason) + "\n")

    @staticmethod
    def init_data():  
        try:
            Id = input("ID:") or None
            name = input("姓名:") or None
            phone = input("电话:") or None
            company = input("公司(可选):") or None
            address = input("地址(可选):") or None
            init = [Id, name, phone, company, address]
            return init
        except ValueError as reason:
            print("WARNING: " + str(reason))

    def add_contacts(self, init): 
        try:
            self.c.execute("INSERT INTO t_adb VALUES(?,?,?,?,?)",
                           (init[0], init[1], init[2], init[3], init[4]))
            self.conn.commit()
            print("INFO: Affected Rows 1\n")
        except sqlite.IntegrityError as reason:
            print("WARNING: " + str(reason) + "\n")
        except TypeError as reason:
            print("WARNING: " + str(reason) + "\n")
        except sqlite.OperationalError as reason:
            print("WARNING: " + str(reason))
            print("请先执行创建表操作...\n")

    @staticmethod
    def input_name():
        name = input("输入姓名:")
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
        except sqlite.OperationalError as reason:
            print("WARNING: " + str(reason))
            print("请先执行创建表操作...\n")

    def delete_by_name(self, name):
        try:
            self.c.execute("DELETE FROM t_adb WHERE name='{}'".format(name))
            self.conn.commit()
            print("INFO: Affected Rows 1\n")
        except sqlite.OperationalError as reason:
            print("WARNING: " + str(reason))
            print("请先执行创建表操作...\n")

    @staticmethod
    def show_menu():
        print("通讯录")
        print("1.创建表")
        print("2.新增")
        print("3.查询")
        print("4.删除")
        print("0.退出")
        
    def main(self): 
        while True:
            self.show_menu()
            try:   
                opt = int(input("你的操作:"))
            except ValueError:
                print("WARNING: Illegal string\n")
                continue
            if opt == 0:
                print("成功退出系统...")
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
    connect = ConnDB()
    connect.main()
    connect.close()
