def personal_info():
    info = dict()
    print("---XX比赛个人信息表---")
    info["姓名"] = input("请输入姓名:")
    info["性别"] = input("请输入性别:")
    info["年龄"] = input("请输入年龄:")
    return info

    

def print_info(info):
    print("我的名字{},今年{}岁,性别{},喜欢敲代码。\n" .format(info["姓名"], info["年龄"], info["性别"]))



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





li = [11, 22, 33, 22, 22, 44, 55, 77, 88, 99, 11]
__ = li[:]
for _ in __:
    if li.count(_) != 1:
        li.remove(_)
print(li)



li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(li[2::3])



s = 'python java php'
print(s.split(' ')[1])