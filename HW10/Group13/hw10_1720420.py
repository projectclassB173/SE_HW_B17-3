import sqlite3
conn = sqlite3.connect('D:\\PYTHON代码\\HW10\\test.db')
print("Opened database successfully");
conn.execute('''CREATE TABLE test 
(ID INT PRIMARY KEY     NOT NULL, 
NAME           TEXT    NOT NULL,  
TELEPHONE      CHAR(15) NOT NULL,
COMPANY        TEXT    NOT NULL,
ADDRESS        TEXT    NOT NULL);''')
print("Table USER created successfully");
conn.execute("INSERT INTO test (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
    VALUES (1, '小明', 123456789, '公司1','地址1')")
conn.execute("INSERT INTO test (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
    VALUES (2, '小王', 987654321, '公司2','地址2')")
conn.execute("INSERT INTO test (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
    VALUES (3, '小李', 987666621, '公司3','地址3')")
conn.execute("INSERT INTO test (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
    VALUES (4, '小方', 999654321, '公司4','地址4')")
conn.commit()
num=conn.total_changes
print("{0} rows changed in table test.".format(num))
conn = sqlite3.connect('D:\\PYTHON代码\\HW10\\test.db')
print("Opened database successfully")
cursor1 = conn.execute("SELECT ID,NAME,TELEPHONE,COMPANY,ADDRESS from test where NAME='小明'")
for row in cursor1:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("TELEPHONE = ", row[2])
    print("COMPANY = ", row[3])
    print("ADDRESS = ", row[4])
conn.execute("delete from test where NAME='小明'")
conn.commit()
print("Total number of rows updated :", conn.total_changes)
num=conn.total_changes
print("{0} rows changed in table USER.".format(num))