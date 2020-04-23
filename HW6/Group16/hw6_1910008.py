import re
# 1.将给定字符串的PHP替换为Python
# best_language = "PHP is the best programming language in the world! "
best_language = "PHP is the best programming language in the world! "
gj = best_language.replace('PHP', 'Python')
print(gj)
print("--------------------------------------------------------------------")

# 2.编写代码，提示用户输入1 - 7
# 七个数字，分别代表周一到周日，打印输出“今天是周几”
gj1 = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
day = int(input('请输入1-7:'))
print(gj1[day - 1])
print("--------------------------------------------------------------------")

# 3.给定一个字符串： Python is the BEST programming Language！
# 编写一个正则表达式用来判断该字符串是否全部为小写。
string = 'Python is the BEST programming Language！'
reg = r'^[a-z\s]+$'
if re.match(reg, string):
    print('字符串全部为小写')
else:
    print('字符串不全为小写')
print("--------------------------------------------------------------------")

# 4.读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：
# （xxx） xxx - xxxx或xxx - xxx - xxxx。
gj2 = '电话为(021)111-2222 111-333-4444 (187)555-5555 123-456-7890'
m = re.findall(r'\d{3}-\d{3}-\d{4}', gj2)
m1 = re.findall(r'[(]\d{3}[)]\d{3}-\d{4}', gj2)
if m is not None:
    print(m)
if m1 is not None:
    print(m1)
print("--------------------------------------------------------------------")

# 5.利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy - mm - dd。
# '今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25',
gj3 = '今天是2022/9/24, 今天是2017/09/25, 今天是2012-07-25, 今天是2020年04月25'
a = re.findall(r'\d{4}-\d{2}-\d{2}', gj3)
for each in a:
    print(each)

