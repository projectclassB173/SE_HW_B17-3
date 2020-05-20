import sqlite3 
conn = sqlite3.connect('E:\\代码\\VSCode代码\\PYTHON代码\\项目实战\\每周作业\\addressbook.db') 
print("Opened database successfully");

conn.execute('''CREATE TABLE addressbook 
(ID INT PRIMARY KEY     NOT NULL, 
NAME           TEXT    NOT NULL,  
TELEPHONE      CHAR(50) NOT NULL,
COMPANY        TEXT    NOT NULL,
ADDRESS        TEXT    NOT NULL);''') 
print("Table USER created successfully");

conn.execute("INSERT INTO addressbook (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
    VALUES (1, '甲', 11111111, '甲公司','甲地址')")
conn.execute("INSERT INTO addressbook (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
    VALUES (2, '乙', 22222222, '乙公司','乙地址')") 
conn.commit() 
num1=conn.total_changes 
print("{0} rows changed in table addressbook.".format(num1))   

conn = sqlite3.connect('E:\\代码\\VSCode代码\\PYTHON代码\\项目实战\\每周作业\\addressbook.db') 
print("Opened database successfully") 
cursor1 = conn.execute("SELECT ID,NAME,TELEPHONE,COMPANY,ADDRESS from addressbook where NAME='甲'") 
for row in cursor1: 
    print("ID = ", row[0]) 
    print("NAME = ", row[1]) 
    print("TELEPHONE = ", row[2]) 
    print("COMPANY = ", row[3])
    print("ADDRESS = ", row[4])

conn.execute("delete from addressbook where NAME='甲'") 
conn.commit() 
print("Total number of rows updated :", conn.total_changes) 
num1=conn.total_changes 
print("{0} rows changed in table USER.".format(num1)) 

