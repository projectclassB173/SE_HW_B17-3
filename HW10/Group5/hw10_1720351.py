import sqlite3

class ConnDB:
    def __init__(self):
        self.conn = sqlite3.connect("connect.db")
        self.sql = self.conn.cursor()

        while True:
            print("1.创建表\n2.新增联系人\n3.按姓名查询\n4.删除联系人\n")
            opt = input("Your select:")
            if opt == '1':
                self.__create_table()
            elif opt == '2':
                self.__add_contacts(self.__init_data())
            elif opt == '3':
                self.__find_name(self.__input_name())
            elif opt == '4':
                self.__delete_name(self.__input_name())

    def close(self):
        self.sql.close()
        self.conn.close()

    def __create_table(self):
        try:
            self.sql.execute('''CREATE TABLE list
                (id INTEGER NOT NULL PRIMARY KEY,
                name TEXT NOT NULL,
                tel TEXT NOT NULL ,
                company TEXT NULL ,
                address TEXT NULL);''')
            self.conn.commit()
            print("Success")
        except:
           pass

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

    def __add_contacts(self, init):  # 传入之前用户输入的内容
        try:
            self.sql.execute("INSERT INTO list(id, name, tel, company, address) VALUES(?,?,?,?,?)", (init[0], init[1], init[2], init[3], init[4]))
            self.conn.commit()
            print("Added")
        except:
            pass

    def __input_name(self):
        name = input("Please input name:")
        return name

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
