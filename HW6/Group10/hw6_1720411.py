#��Ŀ<1>
best_language = "PHP is the best programming language in the world! "
print(best_language.replace("PHP","Python"))

#��Ŀ<2>
cus_input = input("������1-7���֣�")
print("��������{}".format(cus_input))

#��Ŀ<3>
import re

s = 'Python is the BEST programming Language��'
an = re.search('^[a-z]+$ ', s)
print(an)
if an == 'None':
    print(s + '��ȫ��Сд��')
else:
    print('s:', s, 'ȫΪСд')

#��Ŀ<4>
#data.txt�б��������µļ���
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
#��Ŀ<5>
import re
data='������2017/09/25'
print(data)
a=re.findall('(\d{4}[-/��]\d{1,2}[-/��]\d{1,2})',data)
print(re.sub('[-/����]','-',str(a)))