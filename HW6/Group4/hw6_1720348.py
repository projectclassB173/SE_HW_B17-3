# 1.将给定字符串的PHP替换为Python
best_language = "PHP is the best programming language in the world! "
print(best_language.replace("PHP","Python"))

# 2.编写代码，提示用户输入1 - 7
# 七个数字，分别代表周一到周日，打印输出“今天是周几”
c = input("请输入1-7数字：")
print("今天是周{}".format(c))

# 3.给定一个字符串： Python is the BEST programming Language！
# 编写一个正则表达式用来判断该字符串是否全部为小写。
str = "Python is the BEST programming Language！"
a = re.search('^[a-z]+$', str)
if a:
    print("全为小写")
else:
    print("不全为小写")

# 4.读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：
# （xxx） xxx - xxxx或xxx - xxx - xxxx。
import re
s1 = "Phone number is (000)123-1234 , 023-234-4567 , 1111-333-5555 "
result = re.findall(r'([(]\d{3}[)]|\d{3})-?(\d{3})-(\d{4})', s1)
for each in result:
    print(each[0], each[1], each[2], sep="-")

# 5.利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy - mm - dd。
import re
s2 = '今天是2022/9/24,今天是2017/09/25,今天是2012-07-25,今天是2020年04月25'
d = re.findall(r'\d{4}-\d?\d-\d?\d', s2)
for each in d:
    print(each)