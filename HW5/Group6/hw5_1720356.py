题目<1>
name = input("请输入姓名：")
gender = input("请输入性别：")
age = input("请输入年龄：")
dic = {}
dic.update({"姓名": name, "性别": gender, "年龄": age})

题目<2>
print("我的名字{}，今年{}岁，性别{}，喜欢敲代码".format(dic["姓名"], dic["年龄"], dic["性别"]))

题目<3>
height = input("请输入您的身高：")
telenub = input("请输入您的联系方式：")
dic.update({"身高": height, "联系方式": telenub})
print(dic)

题目<4>
for i in dic:
    print("{}:{}".format(i,dic[i]))

题目<5>
li = [11, 22, 33, 22, 22, 44, 55, 77, 88, 99, 11]
s = set(li)
li = list(s)
print("元素的数量有："+str(len(li)))

题目<6>
list=[1,2,3,4,5,6,7,8,9]
list[2::3]

题目<7>
s = 'python java php'
print(s[7:11])
