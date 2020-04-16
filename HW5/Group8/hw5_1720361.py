# 1.某比赛需要获取你的个人信息,设计一个程序,
# 运行时分别提醒用户输入、姓名、性别、年龄,输入完了,请将数据存储为一个字典.


def personal_info():
    info = dict()
    print("---XX比赛个人信息表---")
    info["姓名"] = input("请输入姓名:")
    info["性别"] = input("请输入性别:")
    info["年龄"] = input("请输入年龄:")

    return info


# 2.数据存储完了，然后输出个人介绍:
def print_info(info):
    print("我的名字{},今年{}岁,性别{},喜欢敲代码。\n" .format(info["姓名"], info["年龄"], info["性别"]))


# 3.有一个人对你很感兴趣,平台需要您补足您的身高和联系方式；
# 要求提醒用户输入身高、联系方式,把数据添加到1中创建的字典.
def add_info(info):
    print("有一个人对你很感兴趣,平台需要您补足您的身高和联系方式.")
    info["身高"] = input("请输入身高:")
    info["联系方式"] = input("请输入联系方式:")
    print("")

    return info


def print_all_info(info):
    print("---个人信息---")
    for key in info:
        print("{}:{}" .format(key, info[key]))
    print("")


information = personal_info()
print_info(information)
add_info(information)
print_all_info(information)

# 5.当前有一个列表 li = [11,22,33,22,22,44,55,77,88,99,11]
# 请去除重复元素之后，再统计元素的数量
# 方法1
li = [11, 22, 33, 22, 22, 44, 55, 77, 88, 99, 11]
li2 = li[:]
for each in li2:
    if li.count(each) != 1:
        li.remove(each)
print("5.当前有一个列表 li = [11,22,33,22,22,44,55,77,88,99,11],请去除重复元素之后，再统计元素的数量")
print("方法1:", len(li))

# 方法2
li = [11, 22, 33, 22, 22, 44, 55, 77, 88, 99, 11]
li3 = list()
for each in li:
    if each not in li3:
        li3.append(each)
print("方法2:", len(li3))
print("")


# 6.li = [1,2,3,4,5,6,7,8,9] 请通过切片得出结果 [3,6,9]
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
li2 = li[2::3]
print("6.li = [1,2,3,4,5,6,7,8,9] 请通过切片得出结果 [3,6,9]")
print("切片结果:", li2)
print("")


# 7.s = 'python java php',通过切片获取: ‘java’
s = 'python java php'
s1 = s[6:11]
print("7.s = 'python java php',通过切片获取: ‘java’")
print("切片结果:", s1)