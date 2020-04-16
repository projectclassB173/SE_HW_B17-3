#1.
dict = {}
dict['name'] = input("请输入姓名:")
dict['gender'] = input("请输入性别:")
dict['age'] = input("请输入年龄:")
dic.update({"name": name, "gender": gender, "age": age})

#2.
def print_info(info):
    print("我的名字{},今年{}岁,性别{},喜欢敲代码。\n" .format(info["姓名"], info["年龄"], info["性别"]))

#3.
print("有一个人对你很感兴趣,平台需要您补足您的身高和联系方式.")
height = input("请输入身高:")
phone = input("请输入联系方式:")
dict.update({"姓名": name, "性别": sex, "年龄": age,"身高": height,"联系方式":phone})

#4.
for item in dict:
    print("{}: {}".format(item, dict[item]))

#5.
li = [11, 22, 33, 22, 22, 44, 55, 77, 88, 99, 11]
s = set(li)
li = list(s)
print(len(li))

#6.
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(li[2::3])

#7.
s = 'python java php'
print(s[7:11])