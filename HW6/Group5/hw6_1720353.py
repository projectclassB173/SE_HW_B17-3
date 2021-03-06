import re
# 1.将给定字符串的PHP替换为Python
s = "PHP is the best programming language in the world! "
print(s.replace("PHP", "Python"))
print("------------")


# 2.编写代码，提示用户输入1 - 7
# 七个数字，分别代表周一到周日，打印输出“今天是周几”
print("今天是周{}" .format(["一", "二", "三", "四", "五", "六", "七"][int(input("输入1-7:"))-1]))
print("------------")

# 3.给定一个字符串： Python is the BEST programming Language！
# 编写一个正则表达式用来判断该字符串是否全部为小写。
s = "Python is the BEST programming Language！"
a = re.search('^[a-z]+$', s)
if a:
    print("全为小写")
else:
    print("不全为小写")
print("------------")

# 4.读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：
#（xxx） xxx - xxxx或xxx - xxx - xxxx。
s = "Phone number is (0215)123-1234 , 056-234-4567 , 074-457-9878 , (020)475-7542"
result = re.findall(r'([(]\d{3}[)]|\d{3})-?(\d{3})-(\d{4})', s)
for each in result:
    print(each[0], each[1], each[2], sep="-")
print("------------")

# 5.利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy - mm - dd。
s = '今天是2022/9/24,今天是2017/09/25,今天是2012-07-25,今天是2020年04月25'
date = re.findall(r'\d{4}-\d?\d-\d?\d', s)
for each in date:
    print(each)
