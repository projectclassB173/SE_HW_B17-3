import sqlite3

conn = sqlite3.connect('zh.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE USER 
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       TELEPHONE           CHAR(15)     NOT NULL,
       COMPANY        TEXT    NOT NULL,
       ADDRESS        TEXT    NOT NULL);''')
print("Table created successfully")

conn.execute("INSERT INTO USER (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
      VALUES (1, '赵', 12345678910, 'Z氏公司', '北京' )")
conn.execute("INSERT INTO USER (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
      VALUES (2, '钱', 10987654321, 'Q氏公司', '上海' )")
conn.execute("INSERT INTO USER (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
      VALUES (3, '孙', 11112222333, 'S氏公司', '广州' )")
conn.execute("INSERT INTO USER (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
      VALUES (4, '李', 44445555666, 'L氏公司', '深圳' )")

conn.commit()
print("Records created successfully")

cursor = conn.execute("SELECT ID,NAME,TELEPHONE,COMPANY,ADDRESS  from USER")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("TELEPHONE = ", row[2])
   print("COMPANY = ", row[3])
   print("ADDRESS = ", row[4], "\n")
print("Operation done successfully","\n")

conn.execute("DELETE from USER where ID=1;")
conn.commit()
print("Total number of rows deleted :", conn.total_changes)

cursor = conn.execute("SELECT ID,NAME,TELEPHONE,COMPANY,ADDRESS  from USER")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("TELEPHONE = ", row[2])
   print("COMPANY = ", row[3])
   print("ADDRESS = ", row[4], "\n")
   
print("Operation done successfully")
conn.close()