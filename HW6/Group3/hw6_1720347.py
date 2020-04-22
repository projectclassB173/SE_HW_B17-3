#1 将给定字符串的PHP替换为Python
# best_language = "PHP is the best programming language in the world! "
import re;
pattern = 'PHP'
replacement = 'Python'
best_language = "PHP is the best programming language in the world! "
output = re.sub(pattern, replacement, best_language, count=0, flags=0)
print(output)

#2. 编写代码，提示用户输入1 - 7
#七个数字，分别代表周一到周日，打印输出“今天是周几”
number = input("请输入1-7的数字：")
list = ("周一", "周二", "周三", "周四", "周五", "周六", "周日")
a = int(number)
print("今天是{}".format(list[a-1]))

#3. 给定一个字符串：
#Python is the BEST programming Language！
#编写一个正则表达式用来判断该字符串是否全部为小写。
import re;
str1 = 'Python is the BEST programming Language！'
a = re.match('[a-z]+$', str1)
if a:
    print('全是小写')
else:
    print('不全是小写')

#4. 读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：
#（xxx） xxx - xxxx或xxx - xxx - xxxx。
str2 = '我的电话号码是 189-629-0032 ，有事请拨打此号码联系我。我妈的电话号码是180-618-0525，座机是(000)850-3381。'
pat = re.findall(r'([(]\d{3}[)]|\d{3})-?(\d{3})-(\d{4})', str2)
for item in pat:
    print(item[0], item[1], item[2], sep='-')

#5. 利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy - mm - dd。
#   '今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25',
import re;
str2 = '今天是2022/9/24''今天是2017/09/25''今天是2012-07-25''今天是2020年04月25'
result = re.findall(r'(\d{4})-(\d{2})-(\d{2})', str2)
for item in result:
    print(item[0], item[1], item[2],sep='-')
