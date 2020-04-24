﻿#1
# 将给定字符串的PHP替换为Python  
best_language = "PHP is the best programming language in the world! "
print(best_language.replace("PHP","Python"))

#2
# 编写代码，提示用户输入1-7七个数字，分别代表周一到周日，打印输出“今天是周几”
cus_input = input("请输入1-7数字：")
print("今天是周{}".format(cus_input))

#3
# 给定一个字符串： Python is the BEST programming Language！
# 编写一个正则表达式用来判断该字符串是否全部为小写。
import re
s1='Python is the BEST programming Language！'
an=re.search('^[a-z]+$',s1)
if an:
    print 's1:', an.group(), '全为小写' 
else:
    print s1, "不全是小写！"

#4
# 读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：
#（xxx） xxx-xxxx或xxx-xxx-xxxx。
#data.txt中保存了如下的几行
#187-183-4562
#123 466 7892
#(183) 456-7820
import re
def setPhoneNumber():
    phoneLines = open(r".\.\data.txt","r")
    for phoneLine in phoneLines:
        phoneLine = phoneLine.strip('\n')
        if re.findall("(\d{3})\-(\d{3})\-(\d{4})", phoneLine):
            print phoneLine
        if re.findall("\((\d{3})\)\s(\d{3})\-(\d{4})", phoneLine):
            print phoneLine
if __name__=="__main__":
    setPhoneNumber()

#5
# 利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy-mm-dd。
# '今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25',
import re
data="今天是2022/9/24,今天是2017/09/25,今天是2012-07-25,今天是2020年04月25"
patten_1 = re.compile('(\d{4}[-/]\d{1,2}[-/]\d{1,2})')
date = patten_1.findall(data)[0]
print(date)