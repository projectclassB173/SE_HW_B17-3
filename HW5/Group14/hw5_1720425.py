'''
1、某比赛需要获取你的个人信息，设计一个程序，
运行时分别提醒用户输入 姓名、性别、年龄，输入完了，请将数据存储为一个字典，

2、数据存储完了，然后输出个人介绍，格式如下: 
我的名字XXX，今年XXX岁，性别XX，喜欢敲代码

3、有一个人对你很感兴趣，平台需要您补足您的身高和联系方式； 要求提醒用户输入身高、联系方式，把数据添加到1中创建的字典。

4、用循环输出任务3完成后的字典中的所有信息，格式如下（5项数据之间没有顺序要求）：
姓名：xxx
性别：xxx
年龄：xx
身高：xx
联系方式：xx

5、当前有一个列表 li = [11,22,33,22,22,44,55,77,88,99,11]，请去除重复元素之后，再统计元素的数量

6、li = [1,2,3,4,5,6,7,8,9] 请通过切片得出结果 [3,6,9]

7、s = 'python java php',通过切片获取: ‘java’
'''

#1
name = input("请输入姓名：")
gender = input("请输入性别：")
age = input("请输入年龄：")
dic = {"姓名":name, "性别":gender, "年龄":age}

#2
print("我的名字",name,"，今年",age,"岁，性别",gender,"，喜欢敲代码")

#3
height = input("请输入身高：")
contact = input("请输入联系方式：")
dic["身高"] = height
dic["联系方式"] = contact

#4
for key in dic:
    print(key,"：",dic[key],sep="")

#5
li = [11,22,33,22,22,44,55,77,88,99,11]
li2 = []
'''for i in range(len(li)):
    for j in range(i, len(li)):
        print("长度:",len(li))
        if li[j+1] == li[i]:
            del li[j]
'''
for item in li:
    if item not in li2:
        li2.append(item)
print("去除重复元素之后，列表为：",li2)
print("去除重复元素之后，元素的数量为：",len(li2))

#6
li = [1,2,3,4,5,6,7,8,9]
print(li[2:len(li):3])

#7
s = 'python java php'
print(s[7:11])
