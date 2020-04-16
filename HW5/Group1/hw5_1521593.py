#1. 某比赛需要获取你的个人信息，设计一个程序，
#运行时分别提醒用户输入 姓名、性别、年龄 ，输入完了，请将数据存储为一个字典，
def personal_info():
    info=dict()
    print("比赛需要您的个人信息，请填写个人信息")
    info["姓名"]=input("姓名：")
    info["性别"]=input("性别：")
    info["年龄"]=input("年龄：")
    return info

#2、数据存储完了，然后输出个人介绍，格式如下:
#我的名字XXX，今年XXX岁，性别XX，喜欢敲代码
def print_personal_info(info):
    print("我的名字{},今年{}岁，性别{}，喜欢敲代码\n".format(info["姓名"],info["年龄"],info["性别"]))

#3. 有一个人对你很感兴趣，平台需要您补足您的身高和联系方式； 要求提醒用户输入身高、联系方式，把数据添加到1中创建的字典。
def add_info(info):
    print("有一个人对你很感兴趣，平台需要补充您的联系方式和身高")
    info["身高"]=input("请输入您的身高：")
    info["联系方式"]=input("请输入联系方式：")
    return info

'''4 用循环输出任务3完成后的字典中的所有信息，格式如下（5项数据之间没有顺序要求）：
姓名 ： xxx
性别： xxx
年龄： xx
身高： xx
联系方式：xx
'''
def print_info(info):
    print("----个人信息-----")
    for key in info:
        print("{}：{}".format(key,info[key]))

#5. 当前有一个列表 li = [11,22,33,22,22,44,55,77,88,99,11]，请去除重复元素之后，再统计元素的数量
def count():
    li=[11,22,33,22,22,44,55,77,88,99,11]
    li2=li[:]
    for item in li2:
        if li.count(item)!=1:
            li.remove(item)
    print("列表去除重复元素后，元素的数量为："+str(len(li)))

#6.li = [1,2,3,4,5,6,7,8,9] 请通过切片得出结果 [3,6,9]
def slice1():
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(li[2::3])


#7.s = 'python java php',通过切片获取: ‘java’
def slice2():
    s = 'python java php'
    print(s.split(' ')[1])

