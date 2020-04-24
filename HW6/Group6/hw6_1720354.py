#题目1、将给定字符串的PHP替换为Python
best_language = "PHP is the best programming language in the world! "
print(best_language.replace("PHP","Python"))

#题目2、编写代码，提示用户输入1 - 7，分别代表周一到周日，打印输出“今天是周几”
print("今天是周{}" .format(["一", "二", "三", "四", "五", "六", "七"][int(input("输入1-7:"))-1]))

#题目3、给定一个字符串： Python is the BEST programming Language！编写一个正则表达式用来判断该字符串是否全部为小写。
import re
s = 'Python is the BEST programming Language！'
ss = re.search('^[a-z]+$ ', s)
print(ss)
if ss == 'None':
    print(s + '不全是小写！')
else:
    print('s:', s, '全为小写')

#题目4、读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：（xxx） xxx - xxxx或xxx - xxx - xxxx。
print(" ".join([s for r in re.findall(r"(\(+\d+\)+\d+\-\d+\d+)|(\d+\-\d+\-\d+)","Phone number is (0216)136-1212 , 046-234-4768 , 086-446-9788 , (020)475-7592") for s in r if s!= '']))

#题目5、利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy - mm - dd。
import re
data='今天是2017/09/25'
print(data)
a=re.findall('(\d{4}[-/年]\d{1,2}[-/月]\d{1,2})',data)
print(re.sub('[-/年月]','-',str(a)))