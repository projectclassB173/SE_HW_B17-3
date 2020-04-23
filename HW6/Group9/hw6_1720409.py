# 1.将给定字符串的PHP替换为Python
import re
best_language = "PHP is the best programming language in the world! "
print(best_language.replace("PHP", "Python"))

#结果:Python is the best programming language in the world!

# 2
# 编写代码，提示用户输入1 - 7
# 七个数字，分别代表周一到周日，打印输出“今天是周几”
day=["一","二","三","四","五","六","日"]
number=int(input("输入1-7："))
print("今天是周{}".format(day[number-1]))

#结果:
# 输入1-7：1
# 今天是周一


# 3.给定一个字符串： Python is the BEST programming Language！
# 编写一个正则表达式用来判断该字符串是否全部为小写。
import re
string="Python is the BEST programming Language！"
k=re.search('^[a-z]+$/',string)
if k:
    print("全为小写")
else:
    print("不全为小写")
#结果:不全为小写

# 4.读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：
# （xxx） xxx - xxxx或xxx - xxx - xxxx。
import re
string="Phone Number is 2520-233-541,186-210-5092,(150)522-7542"
result=re.findall(r'([(]\d{3}[)]|\d{3})-?(\d{3})-(\d{4})', string)
for each in result:
    print(each[0],each[1],each[2],sep="-")
#结果：
# 186-210-5092
#(150)-522-7542


# 5.利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy - mm - dd。
# '今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25',
import re
string='今天是2022/9/24, 今天是2017/09/25, 今天是2012-07-25, 今天是2020年04月25'
result=re.findall(r'\d{4}-\d?\d-\d?\d',string)
for each in result:
    print(each)
#结果：
#2012-07-25