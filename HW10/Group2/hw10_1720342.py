import sqlite3
conn = sqlite3.connect('D:\\HY\\HW10\\test.db')
print("数据库成功打开");
conn.execute('''CREATE TABLE test 
(ID INT PRIMARY KEY     NOT NULL, 
NAME           TEXT    NOT NULL,  
TELEPHONE      CHAR(15) NOT NULL,
COMPANY        TEXT    NOT NULL,
ADDRESS        TEXT    NOT NULL);''')
print("用户表创建成功");
conn.execute("INSERT INTO test (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
    VALUES (1, '张三', 18054736981, '腾讯','深圳')")
conn.execute("INSERT INTO test (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
    VALUES (2, '李四', 18316420147, '阿里','浙江')")
conn.execute("INSERT INTO test (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
    VALUES (3, '王五', 17321056912, '华为','东莞')")
conn.commit()
num=conn.total_changes
print("{0} 排已修改完成.".format(num))
conn = sqlite3.connect('D:\\HY\\HW10\\test.db')
print("数据库成功打开")
cursor1 = conn.execute("SELECT ID,NAME,TELEPHONE,COMPANY,ADDRESS from test where NAME='张三'")
for row in cursor1:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("TELEPHONE = ", row[2])
    print("COMPANY = ", row[3])
    print("ADDRESS = ", row[4])
conn.execute("delete from test where NAME='张三'")
conn.commit()
print("数据更新 :", conn.total_changes)
num=conn.total_changes
print("{0} 已更新至用户表.".format(num))