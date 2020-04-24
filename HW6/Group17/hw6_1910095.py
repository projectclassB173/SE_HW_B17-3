1.
best_language = "PHP is the best programming language in the world! "
print(best_language.replace("PHP", "Python"))
print("----------")

2.
number = input("请输入1-7的数字：")
list = ("周一", "周二", "周三", "周四", "周五", "周六", "周日")
a = int(number)
print("今天是{}".format(list[a-1]))

3.
string = "Python is the BEST programming Language！"
a = re.search('^[a-z]+$', string)
if a:
    print("全为小写")
else:
    print("不全为小写")
print("----------")

4.
def setPhoneNumber():
    phoneLines = input('请输入字符串: ')
    for phoneLine in phoneLines:
        phoneLine = phoneLine.strip('\n')
        if re.findall("(\d{3})\-(\d{3})\-(\d{4})", phoneLine):
            print phoneLine
        if re.findall("\((\d{3})\)\s(\d{3})\-(\d{4})", phoneLine):
            print phoneLine


5.
data1='今天是2022/9/24'
data2='今天是2017/09/25'
data3='今天是2012-07-25'
data3='今天是2020年04月25'
patten_1 = re.compile('(\d{4}[-/]\d{1,2}[-/]\d{1,2})')
d1 = re.findall(d1, data1)[0]
d2 = re.findall(d2, data2)[0]
d3 = re.findall(d3, data3)[0]
d4 = re.findall(d4, data4)[0]
print(d1,d2,d3,d4)