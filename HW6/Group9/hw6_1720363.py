# 题目<1>
# 将给定字符串的PHP替换为Python      
# best_language = "PHP is the best programming language in the world! "
best_language = "PHP is the best programming language in the world! "
print(best_language.replace("PHP","Python"))

# 题目<2>
# 编写代码，提示用户输入1-7七个数字，分别代表周一到周日，打印输出“今天是周几”
cus_input = input("请输入1-7数字：")
print("今天是周{}".format(cus_input))

# 题目<3>
# 给定一个字符串： Python is the BEST programming Language！
# 编写一个正则表达式用来判断该字符串是否全部为小写。
import re
s1='Python is the BEST programming Language！'
an=re.search('^[a-z]+$',s1)
if an:
    print(s1,"全部都是小写！")
else:
    print(s1,"没有全部小写！")

# 题目<4>
# 读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：
#（xxx） xxx-xxxx或xxx-xxx-xxxx。
import re
s1=re.search('\d{3}-\d{3,}-\d{4,}','电话号码假定为123-456-1234')
if s1 is not None:
       print(s1.group())

# 题目<5>
# 利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy-mm-dd。
# '今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25',
import re
s1 = '今天是2022/9/24, 今天是2017/09/25, 今天是2012-07-25, 今天是2020年04月25'
an = re.findall(r"(\d{4}-\d{1,2}-\d{1,2})", s1)
print("".join(an))