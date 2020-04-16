dict = {}
dict['name'] = input("Please enter your name:")
dict['gender'] = input("Please enter your gender:")
dict['age'] = input("Please enter your age:")
print("我的名字{}，今年{}岁，性别{}，喜欢敲代码".format(dict['name'], dict['gender'], dict['age']))

dict['height'] = input("Please enter your height:")
dict['phone'] = input("Please enter your phone number:")
for item in dict:
    print("{}: {}".format(item, dict[item]))

li = [11, 22, 33, 22, 22, 44, 55, 77, 88, 99, 11]
s = set()
for item in li:
    s.add(item)
print(len(s))

li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
li = li[li.index(3):len(li)+1:3]
print(li)

s = 'python java php'
s = s[s.index("java") : s.index("java")+len("java")]
print(s)