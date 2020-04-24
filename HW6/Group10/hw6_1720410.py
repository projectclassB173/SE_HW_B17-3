#1将给定字符串的PHP替换为Python   best_language = "PHP is the best programming language in the world! "
best_language = "PHP is the best programming language in the world! "
print(best_language.replace("PHP","Python"))

#2编写代码，提示用户输入1 - 7   七个数字，分别代表周一到周日，打印输出“今天是周几“

cus_input = input("请输入1-7某个数字：")
print("今天是周{}".format(cus_input))


#3给定一个字符串： Python is the BEST programming  Language！
#编写一个正则表达式用来判断该字符串是否全部为小写。
import re
s = 'Python is the BEST programming  Language！'
an = re.search('^[a-z]+$', s)
if an:
   print ('s:', an.group(), '全部是小写')
else:
    print ( '不全是小写')



#4读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：
#（xxx） xxx - xxxx或xxx - xxx - xxxx。
import re

a1 = "number (3432)423-2579 , 275-458-0093 , (383)578-2943"
result = re.findall(r'([(]\d{3}[)]|\d{3})-?(\d{3})-(\d{4})', a1)
for each in result:
    print(each[0], each[1], each[2], sep="-")


#5利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy - mm - dd。

'今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25',
a2 = '今天是2022/9/24,今天是2017/09/25,今天是2012-07-25,今天是2020年04月25'
date = re.findall(r'\d{4}-\d?\d-\d?\d', a2)
for each in date:
    print(each)