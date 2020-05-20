import sqlite3 
conn = sqlite3.connect('C:\\项目实战\\lgj.db') 
print("Opened database successfully");

conn.execute('''CREATE TABLE USER 
(ID INT PRIMARY KEY     NOT NULL, 
NAME           TEXT    NOT NULL,  
TELEPHONE      CHAR(50) NOT NULL,
COMPANY        TEXT    NOT NULL,
ADDRESS        TEXT    NOT NULL);''') 
print("Table USER created successfully");

conn.execute("INSERT INTO USER (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
    VALUES (1, 'zl', 12345678901, 'a公司','长宁')")
conn.execute("INSERT INTO USER (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
    VALUES (2, 'zzy', 98765432123, 'b公司','嘉定')") 

conn.commit() 
num1=conn.total_changes 
print("{0} rows changed in table USER.".format(num1))   

conn = sqlite3.connect('C:\\项目实战\\lgj.db') 
print("Opened database successfully") 

cursor1 = conn.execute("SELECT ID,NAME,TELEPHONE,COMPANY,ADDRESS from USER where NAME='zl'") 
for row in cursor1: 
    print("ID = ", row[0]) 
    print("NAME = ", row[1]) 
    print("TELEPHONE = ", row[2]) 
    print("COMPANY = ", row[3])
    print("ADDRESS = ", row[4])

conn.execute("delete from USER where NAME='zzy'") 
conn.commit() 
print("Total number of rows updated :", conn.total_changes) 
num1=conn.total_changes 
print("{0} rows changed in table USER.".format(num1)) 
