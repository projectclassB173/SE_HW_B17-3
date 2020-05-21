import sqlite3

conn = sqlite3.connect('D:\\test.db')
print("Opened database successfully");

conn.execute('''CREATE TABLE PERSONAL
(ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
TELEPHONE CHAR(11) NOT NULL,
COMPANY TEXT NOT NULL,
ADDRESS TEXT NOT NULL);''')
print("Table PERSONAL created successfully");

conn = sqlite3.connect('D:\\test.db')
print("Opened database successfully");
conn.execute("INSERT INTO CONTACT (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
VALUES (01,'wwj','12345678901', 'ow','shanghai')")
conn.execute("INSERT INTO CONTACT (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
VALUES (02, 'ddj','78963214501', 'mla','changsha')")
conn.commit()
num1 = conn.total_changes
print("{0} 条记录插入.".format(num1))

conn = sqlite3.connect('D:\\test.db')
print("Opened database successfully")
cursor1 = conn.execute("SELECT ID,NAME,TELEPHONE,COMPANY,ADDRESS from CONTACT where NAME = 'wwj'")
for row in cursor1:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("TELEPHONE = ", row[2])
    print("COMPANY = ", row[3])
    print("ADDRESS = ", row[4])

conn = sqlite3.connect('D:\\test.db')
print("Opened database successfully")
conn.execute("delete from CONTACT where NAME='wwj'")
conn.commit()
print("更新的行数:", conn.total_changes)
num1 = conn.total_changes
print("{0} 条记录已删除.".format(num1))

conn.close()