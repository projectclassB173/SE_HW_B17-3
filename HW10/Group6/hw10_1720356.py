import sqlite3 
conn = sqlite3.connect('E:\\Python\\cyh.db') 
print("Opened database successfully");

conn.execute('''CREATE TABLE addressbook 
(ID INT PRIMARY KEY     NOT NULL, 
NAME           TEXT    NOT NULL,  
TELEPHONE      CHAR(50) NOT NULL,
COMPANY        TEXT    NOT NULL,
ADDRESS        TEXT    NOT NULL);''') 
print("Table USER created successfully");

conn.execute("INSERT INTO addressbook (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
    VALUES (1, 'wang', 18208888888, 'xxx','aÇø')")
conn.execute("INSERT INTO addressbook (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
    VALUES (2, 'li', 18918000000, 'yyy','bÇø')") 
conn.commit() 
num1=conn.total_changes 
print("{0} rows changed in table addressbook.".format(num1))   

conn = sqlite3.connect('E:\\Python\\cyh.db') 
print("Opened database successfully") 
cursor1 = conn.execute("SELECT ID,NAME,TELEPHONE,COMPANY,ADDRESS from addressbook where NAME='MINT'") 
for row in cursor1: 
    print("ID = ", row[0]) 
    print("NAME = ", row[1]) 
    print("TELEPHONE = ", row[2]) 
    print("COMPANY = ", row[3])
    print("ADDRESS = ", row[4])

conn.execute("delete from addressbook where NAME='li'") 
conn.commit() 
print("Total number of rows updated :", conn.total_changes) 
num1=conn.total_changes 
print("{0} rows changed in table USER.".format(num1)) 
