'''
1 将给定字符串的PHP替换为Python
best_language = "PHP is the best programming language in the world! "
'''
best_language="PHP is the best programming language in the world!"
print(best_language.replace("PHP","Python"))
print("================")

'''
2 编写代码，提示用户输入1-7七个数字，分别代表周一到周日，打印输出“今天是周几”
'''
day=input("请输入1-7数字：")
print("今天周{}".format(day))
print("===============")

'''
3 给定一个字符串： Python is the BEST programming Language！
编写一个正则表达式用来判断该字符串是否全部为小写。
'''
import re
st="Python is the BEST programming language!"
if re.match('[a-z]+$',st):
    print('全为小写')
else:
    print('不全是小写')
print("====================")

'''
4  读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：
（xxx） xxx-xxxx或xxx-xxx-xxxx。
'''
import re
st='请拨打(254)152-4545或者(132)154-756-8888联系我'
res = re.findall(r'([(]\d{3}[)])(\d{3}-){1,2}(\d{4})', st)
for item in res:
    print(''.join(item))
print('======================')

'''
5 利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy-mm-dd。
'今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25',
'''
st = "今天是2017/09/26"
an=re.findall(r'\d{4}[-/年]\d{2}[-/月]\d{2}',st)
print(re.sub('\D','-',an[0]))
