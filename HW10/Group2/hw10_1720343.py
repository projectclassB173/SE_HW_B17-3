# -*-code:gbk-*-
'''
	build on sqlite3 database
'''
import sqlite3
import os


def CreateDB():
    hcon = sqlite3.connect('Contact.db')
    hcur = hcon.cursor()
    stable = """
	create table contact
	(
        id int(10) primary key,
		name varchar(20) not null,
		telf char(11) not null,
		company varchar(30) not null,
		address varchar(50)
	)
	"""
    hcur.execute(stable)
    hcur.close()
    hcon.close()


def AddInfo(hcon, hcur):
    id = int(input('please input ID: '))
    name = str(input('please input Name: '))
    telf = str(input('please input Tel 1: '))
    company = str(input('please input company: '))
    address = str(input('please input address: '))
    sql = "insert into contact(id,name,telf,company,address) values(?,?,?,?,?)"
    try:
        hcur.execute(sql, (id, name, telf, company, address))
        hcon.commit()
    except:
        hcon.rollback()


def DeleteInfo(hcon, hcur):
    SelectInfo(hcon, hcur)
    did = int(input('please input id of delete: '))
    sql = "delete from contact where id=?"
    try:
        hcur.execute(sql, (did,))
        hcon.commit()
    except:
        hcon.rollback()


def UpdateInfo(hcon, hcur):
    SelectInfo(hcon, hcur)
    did = int(input('please input id of update: '))

    sqlname = "update contact set name=? where id=?"
    name = str(input('please input Name: '))
    try:
        hcur.execute(sqlname, (name, did))
        hcon.commit()
    except:
        hcon.rollback()

    sqltelf = "update contact set telf=? where id=?"
    telf = str(input('please input Tel 1: '))
    try:
        hcur.execute(sqltelf, (telf, did))
        hcon.commit()
    except:
        hcon.rollback()

    sqlcompany = "update contact set tels=? where id=?"
    company = str(input('please input Tel 2: '))
    try:
        hcur.execute(sqlcompany, (company, did))
        hcon.commit()
    except:
        hcon.rollback()

    sqladdress = "update contact set other=? where id=?"
    address = str(input('please input other: '))
    try:
        hcur.execute(sqladdress, (address, did))
        hcon.commit()
    except:
        hcon.rollback()


def SelectInfo(hcon, hcur):
    hcur.execute("select * from contact where name =")
    result = hcur.fetchall()
    print(result)


def Meau():
    print('1.diaplay')
    print('2.add')
    print('3.update')
    print('4.delete')
    print('5.cls')
    print('0.exit')
    sel = 9
    while (sel > 5 or sel < 0):
        sel = int(input('please choice: '))
    return sel


def main():
    if os.path.exists('Contract.db') == False:
        CreateDB()
    hcon = sqlite3.connect('Contract.db')
    hcur = hcon.cursor()
    while (True):
        sel = Meau()
        if (sel == 1):
            SelectInfo(hcon, hcur)
        elif (sel == 2):
            AddInfo(hcon, hcur)
        elif (sel == 3):
            UpdateInfo(hcon, hcur)
        elif (sel == 4):
            DeleteInfo(hcon, hcur)
        elif (sel == 5):
            os.system('cls')
        else:
            break
        print('-------------------------')
    hcur.close()
    hcon.close()


if __name__ == "__main__":
    main()
