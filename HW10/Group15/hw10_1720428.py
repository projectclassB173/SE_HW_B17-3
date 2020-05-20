import sqlite3
def create_table(conn):
    conn.execute('''CREATE TABLE CONVT
    (id integer primary key AUTOINCREMENT,
    name text not null,
    TELPHONE text,
    COMPANY text,
    ADRESS text);''')
    conn.commit()
   
    print('数据库表创建成功')
def add_man(name,tel,comp,ads,conn):
    conn.execute("INSERT INTO CONVT (NAME,TELPHONE,COMPANY,ADRESS) VALUES ('"+name+"', '"+tel+"', '"+comp+"', '"+ads+"')")
    conn.commit()
    num1=conn.total_changes
    print("Insert operation successfully.")
    
def queryname(conn,name):
    sql="select * from CONVT where name='%s'" % (name)
    cur=conn.execute(sql)
    print('{}的联系信息：'.format(name))
    for row in cur:
        print(row)
    cur.close()

def delt(conn,name):
    cursor1 = conn.execute("delete from CONVT where NAME ='"+name+"'")
    num1=conn.total_changes
    print("Contact "+name+" delete successfully")

def main():
    conn=sqlite3.connect("yjqsjk.db")
    create_table(conn)
    add_man('yjq','120','wdfgaah','sasdaaddasdsds',conn)
    add_man('yqq','130','wdfgh','sasdaddddsds',conn)
    add_man('yjj','140','wdfsgh','sasdassds',conn)
    add_man('yyq','110','wdfgddh','sasdassssds',conn)
    queryname(conn,'yjq')
    delt(conn,'yjj')
if __name__ == '__main__':
    main()
