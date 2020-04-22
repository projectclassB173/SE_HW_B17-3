import re
#1
#将给定字符串的PHP替换为Python
#best_language = "PHP is the best programming language in the world! "
print ("第一题：")
best_language='PHP is the best programming language in the world!'
print (best_language)
best_language2=best_language.replace("PHP","Python")   #两个参数都作为一个整体
print (best_language2)
print ("----------")
#2
#编写代码，提示用户输入1 - 7
#七个数字，分别代表周一到周日，打印输出“今天是周几”
print ("第二题：")
day = ["一", "二", "三", "四", "五", "六", "日"]
num = int(input("请输入数字，范围为1-7："))
print ("今天是周{}".format(day[num-1]))
print ("----------")
#3
#给定一个字符串： Python is the BEST programming Language！
#编写一个正则表达式用来判断该字符串是否全部为小写。
print ("第三题：")
text = "Python is the BEST programming Language！"
match =re.search('^[a-z]+$',text)
if match:
    print("字符串中全为小写")
else:
    print("字符串中不全为小写")
print ("----------")
#4
#读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：（xxx） xxx - xxxx或xxx - xxx - xxxx。
print ("第四题：")
telNum ="Phone number is (021)588-6235,125-154-698,135-126-5285,(020)475-7542"
result = re.findall(r'([(]\d{3}[)]|\d{3})-(\d{3})-(\d{4})', telNum)
for item in result:
    print(item[0], item[1],item[1], sep='-')
print ("----------")
#5
#利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy - mm - dd。
#'今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25',
print ("第五题：")
data="今天是2022/9/24,今天是2017/09/25,今天是2012-07-25,今天是2020年04月25"
patten_1 = re.compile('(\d{4}[-/]\d{1,2}[-/]\d{1,2})')
date = patten_1.findall(data)[0]
print(date)