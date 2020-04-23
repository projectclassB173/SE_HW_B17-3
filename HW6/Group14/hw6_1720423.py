'''
1、将给定字符串的PHP替换为Python
best_language = "PHP is the best programming language in the world!"
2、编写代码，提示用户输入1-7七个数字，分别代表周一到周日，打印输出“今天是周几”
3、给定一个字符串： Python is the BEST programming Language!
编写一个正则表达式用来判断该字符串是否全部为小写。
4、读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：
(xxx)xxx-xxxx或xxx-xxx-xxxx。
5、利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy-mm-dd。
'今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25'。
'''

# 1.将给定字符串的PHP替换为Python
best_language = "PHP is the best programming language in the world! "
print(best_language.replace("PHP", "Python"))
print("----------")

# 2.编写代码，提示用户输入1 - 7
# 七个数字，分别代表周一到周日，打印输出“今天是周几”
day = ["一", "二", "三", "四", "五", "六", "七"]
num = int(input("请输入整数1-7:"))
print("今天是周{}" .format(day[num-1]))
print("----------")

# 3.给定一个字符串： Python is the BEST programming Language！
# 编写一个正则表达式用来判断该字符串是否全部为小写。
import re
string = "Python is the BEST programming Language！"
if len(re.findall("[A-Z]", string))>0:
    print("全为小写")
else:
    print("不全为小写")


# 4.读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：
# （xxx） xxx - xxxx或xxx - xxx - xxxx。
import re
s1 = "Phone number is (0215)123-1234 , 056-234-4567 , 074-457-9878 , (020)475-7542"
result = re.findall(r'([(]\d{3}[)]|\d{3})-?(\d{3})-(\d{4})', s1)
for each in result:
    print(each[0], each[1], each[2], sep="-")
print("----------")

# 5.利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy - mm - dd。
import re
s = '今天是2022/9/24,今天是2017/09/25,今天是2012-07-25,今天是2020年04月25'
d = re.findall(r'\d{4}-\d?\d-\d?\d', str1)
for each in d:
    print(each)
print("-----END-----")
    
