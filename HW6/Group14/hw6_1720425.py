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


#1----------------------------------------------------------------------------------
best_language = "PHP is the best programming language in the world!"
print(best_language.replace("PHP", "Python"))


#2----------------------------------------------------------------------------------
days = ["一", "二", "三", "四", "五", "六", "日"]
day = int(input("请输入1-7范围中的数字："))
try:
    print("今天是周", days[day-1], sep="")
    
except IndexError:
    print("输入的数字不在规定的范围内！")
    
except ValueError:
    print("输入的字符不是数字！")


#3----------------------------------------------------------------------------------
import re

string = "Python is the BEST programming Language!"
if len(re.findall("[A-Z]", string))>0:
    print("该字符串中有大写字母！")
else:
    print("该字符串全部为小写字母！")


#4----------------------------------------------------------------------------------
import re

phoneNumber = input("请输入一串带有电话号码的字符串：")
print(re.findall("(\(\d{3}\)\d{3}\-\d{4})|(\d{3}\-\d{3}\-\d{4})", phoneNumber))


#5----------------------------------------------------------------------------------
import re

dates = ['今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25']
for date in dates:
    result = re.findall("(\d{4}\/\d{1,2}\/\d{1,2})|(\d{4}\-\d{1,2}\-\d{1,2})|(\d{4}年\d{1,2}月\d{1,2})", date)
    if len(result)>0:
        print(result)