#题目<1>
name = input("请输入姓名：")
gender = input("请输入性别：")
age = input("请输入年龄：")
dic = {}
dic.update({"name": name, "gender": gender, "age": age})
#题目<2>
print("我的名字{}，今年{}岁，性别{}，喜欢敲代码".format(dic["name"], dic["gender"], dic["age"]))
#题目<3>
high = input("请输入您的身高：")
mobil_phone = input("请输入您的联系方式：")
dic.update({"high": high, "mobil_phone": mobil_phone})
#题目<4>
for k in dic:
    print(str(k)+':'+str(dic[k]))
#题目<5>
li = [11, 22, 33, 22, 22, 44, 55, 77, 88, 99, 11]
s = set(li)
li = list(s)
print("元素的数量有："+str(len(li)))
#题目<6>
list=[1,2,3,4,5,6,7,8,9]
print(list[2::3])
#题目<7>
s = 'python java php'
print(s[7:11])
