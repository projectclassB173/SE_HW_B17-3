# 1. 某比赛需要获取你的个人信息，设计一个程序，运行时分别提醒用户输入 姓名、性别、年龄 ，输入完了，请将数据存储为一个字典。
name = input("请输入姓名：")
sex = input("请输入性别：")
age = input("请输入年龄：")
dict = {"姓名": name, "性别": sex, "年龄": age}

# 2、数据存储完了，然后输出个人介绍，格式如下: 我的名字XXX，今年XXX岁，性别XX，喜欢敲代码。
print("我的名字{},今年 {} 岁，性别 {},喜欢敲代码".format(dict["姓名"], dict["年龄"], dict["性别"]))

# 3.有一个人对你很感兴趣,平台需要您补足您的身高和联系方式；要求提醒用户输入身高、联系方式,把数据添加到1中创建的字典。
height = input("请输入身高:")
phone = input("请输入联系方式:")
dict.update({"姓名": name, "性别": sex, "年龄": age,"身高": height,"联系方式":phone})

# 4.用循环输出任务3完成后的字典中的所有信息，格式如下（5项数据之间没有顺序要求）：
print("--个人信息--")
for key in dict:
    print("{}:{}".format(key, dict[key]))

# 5.当前有一个列表 li = [11,22,33,22,22,44,55,77,88,99,11]，请去除重复元素之后，再统计元素的数量

li = [11, 22, 33, 22, 22, 44, 55, 77, 88, 99, 11]
for each in li:
    if li.count(each) != 1:
       li.remove(each)
print(str(len(li)))

# 6.li = [1,2,3,4,5,6,7,8,9] 请通过切片得出结果 [3,6,9]
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(li[2::3])

# 7.s = 'python java php',通过切片获取: ‘java’
s = 'python java php'
s1 = s[6:11]
print(s1)