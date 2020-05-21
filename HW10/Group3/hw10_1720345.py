import sqlite3
conn = sqlite3.connect('F:\\PYTHON\\DATA\\test.db')
print("Opened database successfully");
conn.execute('''CREATE TABLE test 
(ID INT PRIMARY KEY     NOT NULL, 
NAME           TEXT    NOT NULL,  
TELEPHONE      CHAR(15) NOT NULL,
COMPANY        TEXT    NOT NULL,
ADDRESS        TEXT    NOT NULL);''')
print("Table USER created successfully");
conn.execute("INSERT INTO test (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
    VALUES (1, '张三', 13856489571, 'A公司','地址1')")
conn.execute("INSERT INTO test (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
    VALUES (2, '李四', 12956879452, 'B公司','地址2')")
conn.execute("INSERT INTO test (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
    VALUES (3, '王五', 15248648799, 'C公司','地址3')")
conn.execute("INSERT INTO test (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
    VALUES (4, '赵六', 17856994233, 'D公司','地址4')")
conn.commit()
num=conn.total_changes
print("{0} rows changed in table test.".format(num))
conn = sqlite3.connect('F:\\PYTHON\\DATA\\test.db')
print("Opened database successfully")
cursor1 = conn.execute("SELECT ID,NAME,TELEPHONE,COMPANY,ADDRESS from test where NAME='张三'")
for row in cursor1:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("TELEPHONE = ", row[2])
    print("COMPANY = ", row[3])
    print("ADDRESS = ", row[4])
conn.execute("delete from test where NAME='张三'")
conn.commit()
print("Total number of rows updated :", conn.total_changes)
num=conn.total_changes
print("{0} rows changed in table USER.".format(num))