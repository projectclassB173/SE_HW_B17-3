##1.某比赛需要获取你的个人信息，设计一个程序，
print("--xxx比赛个人信息--")
name = input("请输入姓名：")
sex = input("请输入性别：")
age = input("请输入年龄：")
dict = {"姓名": name, "性别": sex, "年龄": age}

##2.数据存储完了，然后输出个人介绍:
print("我的名字{},今年 {} 岁，性别 {},喜欢敲代码".format(dict["姓名"], dict["年龄"], dict["性别"]))

##3.有一个人对你很感兴趣，平台需要您补足您的身高和联系方式；
height = input("身高:")
tel = input("联系方式:")
dict ["请输入您的身高"] = height
dict ["请输入您的联系方式"] = tel
print(dict)

##4.用循环输出任务3完成后的字典中的所有信息：
for key in dict:
    print("{}:{}".format(key, dict[key]))
print(" ")

##5.当前有一个列表 li = [11,22,33,22,22,44,55,77,88,99,11]，请去除重复元素之后，再统计元素的数量
li = [11, 22, 33, 22, 22, 44, 55, 77, 88, 99, 11]
newlist = []
for i in li:
    if i not in newlist:
	    newlist.append(i)
print(newlist)
print(len(newlist))

#6.li = [1,2,3,4,5,6,7,8,9] 请通过切片得出结果 [3,6,9]
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(li[2::3])

##7.s = 'python java php',通过切片获取: ‘java’
s = 'python java php'
print(s.split(" ")[1])