#题目<1>
best_language = "PHP is the best programming language in the world! "
print(best_language.replace("PHP","Python"))

#题目<2>
cus_input = input("请输入1-7数字：")
print("今天是周{}".format(cus_input))

#题目<3>
import re

s = 'Python is the BEST programming Language！'
an = re.search('^[a-z]+$ ', s)
print(an)
if an == 'None':
    print(s + '不全是小写！')
else:
    print('s:', s, '全为小写')

#题目<4>
#data.txt中保存了如下的几行
#136-118-1949
#136 118 1949
#(136) 118-1949
import re
def PhoneNumber():
    phoneLines = open(r"data.txt","r")
    for phoneLine in re.split('\n',phoneLines):
        if re.findall("\d{3}\-\d{3}\-\d{4}|\(\d{3}\)\s\d{3}\-\d{4}", phoneLine):
            print(phoneLine)
if __name__=="__main__":
    PhoneNumber()
#题目<5>
import re
data='今天是2017/09/25'
print(data)
a=re.findall('(\d{4}[-/年]\d{1,2}[-/月]\d{1,2})',data)
print(re.sub('[-/年月]','-',str(a)))