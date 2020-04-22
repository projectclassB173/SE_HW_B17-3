import re
''' 
1 将给定字符串的PHP替换为Python
best_language = "PHP is the best programming language in the world! "

Python 的 re 模块提供了re.sub用于替换字符串中的匹配项。
语法：
re.sub(pattern, repl, string, count=0, flags=0)
参数：
pattern : 正则中的模式字符串。
repl : 替换的字符串，也可为一个函数。
string : 要被查找替换的原始字符串。
count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
'''
best_language = "PHP is the best programming language in the world! "
best_language = re.sub(r'PHP', "Python", best_language)
print(best_language)

'''
2 编写代码，提示用户输入1-7七个数字，分别代表周一到周日，打印输出“今天是周几”
'''
day = input("Please enter a number between 1 to 7:")
s = ["一", "二", "三", "四", "五", "六", "日"]
print("今天是周{}".format(s[int(day)-1]))
'''
3 给定一个字符串： Python is the BEST programming Language！
编写一个正则表达式用来判断该字符串是否全部为小写。
'''
s = 'Python is the BEST programming Language！'
pattern = re.search('^[a-z]+$',s)
if pattern:
    print(s, '全为小写')
else:
    print(s, "不全为小写")

'''
4  读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：
（xxx） xxx-xxxx或xxx-xxx-xxxx。
'''
def setPhoneNumber():
    phoneLines = input()
    for phoneLine in phoneLines:
        phoneLine = phoneLine.strip('\n')
        if re.findall("(\d{3})\-(\d{3})\-(\d{4})", phoneLine):
            print(phoneLine)
        if re.findall("\((\d{3})\)\s(\d{3})\-(\d{4})", phoneLine):
            print(phoneLine)
if __name__=="__main__":
    setPhoneNumber()

'''
5 利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy-mm-dd。

'今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25',
'''
import re
data='今天是2022/9/24'
patten_1 = re.compile('(\d{4}[-/]\d{1,2}[-/]\d{1,2})')
date = patten_1.findall(data)[0]
print(date)