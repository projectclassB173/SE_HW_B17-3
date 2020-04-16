1.
def person_information():
    information = dict()
    information = {'name':'','sex':'','age':''}
    information['name'] = input('请输入你的姓名：')
    information['sex'] = input('请输入你的性别：')
    information['age'] = input('请输入你的年龄：')
    return information

2.
def print_information(information):
print("我的名字叫做{person_information['name']}，今年{person_information['age']}岁,性别{person_information['sex']}，喜欢敲代码")

3.
def add_information(information):
information['height'] = input('请输入你的身高：')
information['phone'] = input('请输入你的联系方式：')
print(information)
return information

4.
def print_all_information(information):
    print("---个人信息---")
    for key in information:
        print("{}:{}" .format(key, information[key]))
    print("")

infor = personal_information()
print_information(infor)
add_information(infor)
print_all_information(infor)

5.
li = [11, 22, 33, 22, 22, 44, 55, 77, 88, 99, 11]
li2 = li[:]
for each in li2:
    if li.count(each) != 1:
        li.remove(each)
print("5.当前有一个列表 li = [11,22,33,22,22,44,55,77,88,99,11],请去除重复元素之后，再统计元素的数量")
print(len(li))

6.
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
li2 = li[2::3]
print("6.li = [1,2,3,4,5,6,7,8,9] 请通过切片得出结果 [3,6,9]")
print("切片结果:", li2)
print("")

7.s = 'python java php'
s1 = s[6:11]
print("7.s = 'python java php',通过切片获取: ‘java’")
print("切片结果:", s1)
