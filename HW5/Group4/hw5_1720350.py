<<<<<<< HEAD
'''1. 某比赛需要获取你的个人信息，设计一个程序，

运行时分别提醒用户输入 姓名、性别、年龄 ，输入完了，请将数据存储为一个字典，

2、数据存储完了，然后输出个人介绍，格式如下:

我的名字XXX，今年XXX岁，性别XX，喜欢敲代码

3. 有一个人对你很感兴趣，平台需要您补足您的身高和联系方式； 要求提醒用户输入身高、联系方式，把数据添加到1中创建的字典。

4 用循环输出任务3完成后的字典中的所有信息，格式如下（5项数据之间没有顺序要求）：

姓名 ： xxx

性别： xxx

年龄： xx

身高： xx

联系方式：xx

5. 当前有一个列表 li = [11,22,33,22,22,44,55,77,88,99,11]，请去除重复元素之后，再统计元素的数量

6.li = [1,2,3,4,5,6,7,8,9] 请通过切片得出结果 [3,6,9]

7.s = 'python java php',通过切片获取: ‘java’
'''


#1
=======
#题目 1
>>>>>>> dev
name = input("请输入姓名：")
gender = input("请输入性别：")
age = input("请输入年龄：")
dic = {"姓名":name, "性别":gender, "年龄":age}

<<<<<<< HEAD
#2
print("我的名字",name,"，今年",age,"岁，性别",gender,"，喜欢敲代码")

#3
high = input("请输入您的身高：")
mobil_phone = input("请输入您的联系方式：")
dic.update({"身高": high, "电话": mobil_phone})

#4
for key in dic:
    print(key,"：",dic[key],sep="")

#5
li = [11, 22, 33, 22, 22, 44, 55, 77, 88, 99, 11]
__ = li[:]
for _ in __:
    if li.count(_) != 1:
        li.remove(_)
print(li)

#6
li=[1,2,3,4,5,6,7,8,9]
print(li[2::3])

#7
s='python java php'
print(s[7:11])
=======
#题目 2
print("我的名字{}，今年{}岁，性别{}，喜欢敲代码\n".format(dic["姓名"], dic["性别"], dic[ "年龄"]))

#题目3
height = input("请输入身高：")
mobil_phone = input("请输入联系方式：")
dic["身高"] = height
dic["联系方式"] = mobil_phone

#题目 4
for key in dic:
    print(key,"：",dic[key],sep="")

#题目 5
list = [11, 22, 33, 22, 22, 44, 55, 77, 88, 99, 11]
__ = list[:]
for _ in __:
    if list.count(_) != 1:
        list.remove(_)
print(list)

#题目 6
list=[1,2,3,4,5,6,7,8,9]
print(list[2::3])

#题目 7
s = 'python java php'
print(s[7:11])


>>>>>>> dev
