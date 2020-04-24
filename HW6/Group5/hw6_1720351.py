import re
# 1.将给定字符串的PHP替换为Python
print("PHP is the best programming language in the world! ".replace("PHP", "Python"))

# 2.编写代码，提示用户输入1 - 7
# 七个数字，分别代表周一到周日，打印输出“今天是周几”
print("今天是周{}" .format(["一", "二", "三", "四", "五", "六", "七"][int(input("输入1-7:"))-1]))

# 3.给定一个字符串： Python is the BEST programming Language！
# 编写一个正则表达式用来判断该字符串是否全部为小写。
print("全为小写") if re.search('^[a-z]+$', "Python is the BEST programming Language！") else print("不全为小写")

# 4.读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：
# （xxx） xxx - xxxx或xxx - xxx - xxxx。
print(" ".join([s for r in re.findall(r"(\(+\d+\)+\d+\-\d+\d+)|(\d+\-\d+\-\d+)","Phone number is (0215)123-1234 , 056-234-4567 , 074-457-9878 , (020)475-7542") for s in r if s!= '']))

# 5.利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy - mm - dd。
print("".join([____ for ___ in [r for r in list(zip([__ for _, __ in enumerate(re.findall(r"(\d?\d?\d+)", '今天是2022/9/24,今天是2017/09/25,今天是2012-07-25,今天是2020年04月25')) if _ % 3 == 0 ], ['-', '-', '-', '-'], [__ for _, __ in enumerate(re.findall(r"(\d?\d?\d+)", '今天是2022/9/24,今天是2017/09/25,今天是2012-07-25,今天是2020年04月25')) if _ in [1, 4, 7, 10]], ['-', '-', '-', '-'], [__ for _, __ in enumerate(re.findall(r"(\d?\d?\d+)", '今天是2022/9/24,今天是2017/09/25,今天是2012-07-25,今天是2020年04月25')) if _ in [2, 5, 8, 11]]))] for ____ in ___]).replace("20"," 20").replace("20 20", "2020"))
