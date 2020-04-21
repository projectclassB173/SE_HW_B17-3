best_language = "PHP is the best programming language in the world! "
print(best_language.replace("PHP","Python"))

cus_input = input("请输入1-7数字：")
print("今天是周{}".format(cus_input))

import read
s1 = "Python is the BEST programming Language！"
an = read.search('^[a-z]+$', s1)
if an:
    print("全为小写")
else:
    print("不全为小写")

s2 = "Phone number is (0215)123-1234 , 056-234-4567 , 074-457-9878 , (020)475-7542"
result = read.findall(r'([(]\d{3}[)]|\d{3})-?(\d{3})-(\d{4})', s2)
for each in result:
    print(each[0], each[1], each[2], sep="-")

s3 = '今天是2022/9/24,今天是2017/09/25,今天是2012-07-25,今天是2020年04月25'
date = read.findall(r'\d{4}-\d?\d-\d?\d', s3)
for each in date:
    print(each)
