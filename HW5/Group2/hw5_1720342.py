#1.
dict = {}
dict['name'] = input("请输入姓名:")
dict['gender'] = input("请输入性别:")
dict['age'] = input("请输入年龄:")
dic.update({"name": name, "gender": gender, "age": age})

#2.
print("我的名字{}，今年{}岁，性别{}，喜欢敲代码".format(dict['name'], dict['gender'], dict['age']))

#3.
dict['height'] = input("请输入身高:")
dict['phone'] = input("请输入联系方式:")
dic.update({"high": high, "phone": phone})

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