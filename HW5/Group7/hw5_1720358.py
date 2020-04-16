print("--xxx比赛个人信息--")
name = input("请输入姓名：")
sex = input("请输入性别：")
age = input("请输入年龄：")
dict = {"姓名": name, "性别": sex, "年龄": age}

# 2.
dict = {"姓名": name, "性别": sex, "年龄": age}
print("我的名字{},今年 {} 岁，性别 {},喜欢敲代码".format(dict["姓名"], dict["年龄"], dict["性别"]))

# 3.

print("有一个人对你很感兴趣,平台需要您补足您的身高和联系方式.")
height = input("请输入身高:")
phone = input("请输入联系方式:")
dict.update({"姓名": name, "性别": sex, "年龄": age,"身高": height,"联系方式":phone})

# 4.
print("--个人信息--")
for key in dict:
    print("{}:{}".format(key, dict[key]))

# 5.
li = [11, 22, 33, 22, 22, 44, 55, 77, 88, 99, 11]
li2 = li[:]
for each in li2:
    if li.count(each) != 1:
       li.remove(each)
print("列表 li = [11,22,33,22,22,44,55,77,88,99,11]去除重复元素之后")
print("元素的数量为："+str(len(li)))

# 6.
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
li2 = li[2::3]
print("切片结果:", li2)

# 7.s = 'python java php',通过切片获取: ‘java’
s = 'python java php'
print("切片结果:", s.split(' ')[1])