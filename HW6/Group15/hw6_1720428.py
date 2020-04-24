#1
best_language = "PHP is the best programming language in the world! "
print(best_language.replace("PHP","Python"))
#2
cus_input = input("请输入1-7数字：")
print("今天是周{}".format(cus_input))
#3
import re
s1='Python is the BEST programming Language！'
an=re.search('^[a-z]+$',s1)
if an:
    print ('s1:', an.group(), '全为小写' )
else:
    print (s1, "不全是小写！")
#4
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
import re
data='今天是2022/9/24'
patten_1 = re.compile('(\d{4}[-/]\d{1,2}[-/]\d{1,2})')
date = patten_1.findall(data)[0]
print(date)