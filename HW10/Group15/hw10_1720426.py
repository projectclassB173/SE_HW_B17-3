import sqlite3

class AddressBook:
    def __init__(self):
        self.conn = sqlite3.connect('C:\\Users\\mky\\Desktop\\test.db')
        print("Opened database successfully")
            
    def create_table(self):
        self.conn.execute('''CREATE TABLE CONTACT
        (ID INT PRIMARY KEY     NOT NULL, 
        NAME            TEXT    NOT NULL, 
        TELEPHONE       TEXT    NOT NULL, 
        COMPANY         TEXT,
        ADDRESS         TEXT);''') 
        print("Table CONTACT created successfully")
        self.conn.close()
        
    def insert_table(self,idx=0,name='null',telephone='null',company='null',address='null'):
        try:
            self.conn.execute("INSERT INTO CONTACT (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
                         VALUES('%d', '%s', '%s', '%s', '%s')" % (idx,name,telephone,company,address))
            self.conn.commit() 
            print("Insert operation successfully.") 
        except sqlite3.IntegrityError as reason:
            print("WARNING: " + str(reason) + "\n")
        
    def select_table_by_name(self,name='null'):
        cursor1 = self.conn.execute("SELECT * from CONTACT where NAME = '%s'" % (name))
        for row in cursor1:
            print("ID = ", row[0]) 
            print("NAME = ", row[1]) 
            print("TELEPHONE = ", row[2]) 
            print("COMPANY = ", row[3]) 
            print("ADDRESS = ", row[4]) 
            print("Operation done successfully") 
            
    def select_all(self):
        cursor2 = self.conn.execute("SELECT * from CONTACT")
        for row in cursor2:
            print("ID = ", row[0]) 
            print("NAME = ", row[1]) 
            print("TELEPHONE = ", row[2]) 
            print("COMPANY = ", row[3]) 
            print("ADDRESS = ", row[4]) 
            print("Operation done successfully") 
            
    def delet_table(self,idx=0):
        self.conn.execute("delete from CONTACT where ID = '%s'" % (idx))
        self.conn.commit() 
        print("Operation done successfully") 

a = AddressBook()
a.create_table()
a.insert_table(idx=1,name='MaKaiYue',telephone='11111111111',company='Gench',address='Shanghai')
a.select_all()
a.select_table_by_name('MaKaiYue')
a.delet_table(idx=1)