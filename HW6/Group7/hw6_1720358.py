import re
# 1
s = "PHP is the best programming language in the world! "
print(s.replace("PHP", "Python"))
print("------------")


# 2
# 七个数字，分别代表周一到周日，打印输出“今天是周几”
print("今天是周{}" .format(["一", "二", "三", "四", "五", "六", "七"][int(input("输入1-7:"))-1]))
print("------------")

# 3
# 编写一个正则表达式用来判断该字符串是否全部为小写。
s = "Python is the BEST programming Language！"
a = re.search('^[a-z]+$', s)
if a:
    print("全为小写")
else:
    print("不全为小写")
print("------------")

# 4
#（xxx） xxx - xxxx或xxx - xxx - xxxx。
s = "Phone number is (0215)123-1234 , 056-234-4567 , 074-457-9878 , (020)475-7542"
result = re.findall(r'([(]\d{3}[)]|\d{3})-?(\d{3})-(\d{4})', s)
for each in result:
    print(each[0], each[1], each[2], sep="-")
print("------------")

# 5
s = '今天是2022/9/24,今天是2017/09/25,今天是2012-07-25,今天是2020年04月25'
date = re.findall(r'\d{4}-\d?\d-\d?\d', s)
for each in date:
    print(each)