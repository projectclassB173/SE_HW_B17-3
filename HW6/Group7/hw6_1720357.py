# 1
best_language = "PHP is the best programming language in the world! "
print(best_language.replace("PHP","Python"))

# 2
cus_input = input("输入1~7")
print("今天是周{}".format(cus_input))

# 3
import re
a=re.search("^[a-z]+$","Python is the BEST programming Language！")
if a:
  print("Python is the BEST programming Language！","全部小写")
else:
  print("Python is the BEST programming Language！","没有全部小写")

# 4
import re
zen = "123-456-7890"
m = re.findall("\d", zen)
print(m)

# 5
import re
a= re.compile('(\d{4}[-/]\d{1,2}[-/]\d{1,2})').findall("今天是2022/9/24,今天是2017/09/25,今天是2012-07-25,今天是2020年04月25")[0]
print(a)