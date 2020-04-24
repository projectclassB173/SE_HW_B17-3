#1.将给定字符串的PHP替换为Python      
best_language = "PHP is the best programming language in the world! "
best_language.replace("PHP","Python")
#2.编写代码，提示用户输入1-7七个数字，分别代表周一到周日，打印输出“今天是周几”
num =int(input('请输入1-7之间的数字：'))
if num == 1:
    print('今天是周一')
elif num == 2:
    print('今天是周二')
elif num == 3:
    print('今天是周三')
elif num == 4:
    print('今天是周四')
elif num == 5:
    print('今天是周五')
elif num == 6:
    print('今天是周六')
elif num == 7:
    print('今天是周日')
#3.给定一个字符串： Python is the BEST programming Language！编写一个正则表达式用来判断该字符串是否全部为小写。
import re
s1='Python is the BEST programming Language！'

an=re.search('^[a-z]+$',s1)
if an:
    print ('s1:', an.group(), '全是小写' )
else:
    print (s1, "不全是小写")
#4.读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：（xxx） xxx-xxxx或xxx-xxx-xxxx。
import re

#5.利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy-mm-dd。
#'今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25',
import re
str = "今天是2022/9/24,今天是2017/09/25,今天是2012-07-25,今天是2020年04月25"
s1 = re.compile(r'\d{4}-\d{2}-\d{2}')
s2 = re.findall(s1, s2)
    print(s2)