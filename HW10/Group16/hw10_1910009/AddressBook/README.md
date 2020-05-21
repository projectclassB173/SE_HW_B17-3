# Week 10

## 题目

- 编写一个 Python 程序，采用 SQLite 数据库实现通讯录管理功能。
- 采用 SQLite 数据库存放个人通讯录，要求存放联系人的姓名、电话、公司、地址；
- 设计相应的函数完成以下数据库操作：
  - 创建数据库表；
  - 新增联系人；
  - 按姓名查询联系人详细信息；
  - 删除联系人；

## 运行

### t_person表：

| 属性           | 类型 |
| -------------- | ---- |
| id(pk)         | Int  |
| name(not null) | Text |
| telephone      | Text |
| company        | Text |
| address        | Text |

### Python
```bash
python3.7 manage.py

===== 通讯录管理系统: =====
1. 创建通讯录表
2. 新增联系人
3. 按姓名查询联系人详细信息
4. 删除联系人
5. 退出
输入选项序号：1
Table t_person created successful
===== 通讯录管理系统: =====
1. 创建通讯录表
2. 新增联系人
3. 按姓名查询联系人详细信息
4. 删除联系人
5. 退出
输入选项序号：2
Input id: 1
Input name: Ben
Input telephone: 110
Input company: Google
Input address: Street 1
Add Ben sucessfully
===== 通讯录管理系统: =====
1. 创建通讯录表
2. 新增联系人
3. 按姓名查询联系人详细信息
4. 删除联系人
5. 退出
输入选项序号：2
Input id: 2
Input name: Jack
Input telephone: 119
Input company: Apple
Input address: Road 2
Add Jack sucessfully
===== 通讯录管理系统: =====
1. 创建通讯录表
2. 新增联系人
3. 按姓名查询联系人详细信息
4. 删除联系人
5. 退出
输入选项序号：3
输入要查询的名字:Ben
Id:  1
Name:  Ben
Telephone:  110
Company:  Google
Address:  Street 1
===== 通讯录管理系统: =====
1. 创建通讯录表
2. 新增联系人
3. 按姓名查询联系人详细信息
4. 删除联系人
5. 退出
输入选项序号：4
输入要删除的联系人id:1
Delete successfully
===== 通讯录管理系统: =====
1. 创建通讯录表
2. 新增联系人
3. 按姓名查询联系人详细信息
4. 删除联系人
5. 退出
输入选项序号：5
再见
```
### Sqlite3

```sqlite3
sqlite> .database
main: /Volumes/data_mac/workspace/code/python/11/hw_1910009/AddressBook/address_book.db
sqlite> .table
person    t_person
sqlite> .shema t_person
Error: unknown command or invalid arguments:  "shema". Enter ".help" for help
sqlite> .schema t_person
CREATE TABLE t_person( ID INT primary key, name text not null,       telephone text,company text,address text );
sqlite>
```

Asahi Huang  
2020.05.20

