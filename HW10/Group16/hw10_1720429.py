import sqlite3
conn = sqlite3.connect('C:\Users\hm\sqlite\user.db')
print("Opened database successfully");

conn.execute('''CREATE TABLE user
(id INT PRIMARY KEY     NOT NULL, 
name           TEXT    NOT NULL,  
tel     VERCHAR(50) NOT NULL,
company      TEXT    NOT NULL,
address     TEXT    NOT NULL);''')
print("Table USER created successfully");

conn.execute("INSERT INTO user (id,name,tel,company,address)\
    VALUES (1,'张三',111111,'公司1','上海')")
conn.execute("INSERT INTO user (id,name,tel,company,address)\
    VALUES (2,'李四',2222222,'公司2','北京')")
conn.execute("INSERT INTO user (id,name,tel,company,address)\
    VALUES (3,'王五',3333333,'公司3','南京')")
conn.execute("INSERT INTO user (id,name,tel,company,address)\
    VALUES (4,'马六',4444444,'公司4','深圳')")

conn.commit()
num1=conn.total_changes
print("{0} rows changed in table user.".format(num1))

conn = sqlite3.connect('C:\Users\hm\sqlite\user.db')
print("Opened database successfully")
cursor1 = conn.execute("SELECT id,name,tel,company,address from user where name='张三'")
for row in cursor1:
    print("id = ", row[0])
    print("name = ", row[1])
    print("tel = ", row[2])
    print("company = ", row[3])
    print("address = ", row[4])

conn.execute("delete from user where name='张三'")
conn.commit()
print("Total number of rows updated :", conn.total_changes)
num1=conn.total_changes
print("{0} rows changed in table USER.".format(num1))

