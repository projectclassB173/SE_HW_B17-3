#题目1
def hw1():
    info = dict()
    print("---XX比赛个人信息表---")
    info["姓名"] = input("输入你的姓名：")
    info["性别"] = input("输入你的性别：")
    info["年龄"] = input("输入你的年龄：")
    return info
    
#题目2
def hw2(info):
    print("我的名字{},今年{}岁,性别{},喜欢敲代码。\n" .format(info["姓名"], info["年龄"], info["性别"]))

#题目3
def hw3(info):
    print("有一个人对你很感兴趣,平台需要您补足您的身高和联系方式.")
    info["身高"] = input("输入你的身高：")
    info["联系方式"] = input("输入的联系方式：")
    return info

#题目4
def hw4(info):
    print("---个人信息---")
    for key in info:
        print("{}:{}" .format(key, info[key]))
    print("")

information = hw1()
hw2(information)
hw3(information)
hw4(information)

#题目5
list1 = [11, 22, 33, 22, 22, 44, 55, 77, 88, 99, 11]
__ = list1[:]
for _ in __:
    if list1.count(_) != 1:
        list1.remove(_)
print(list1)

#题目6
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list2[2::3])

#题目
s = 'python java php'
print(s.split(' ')[1])
