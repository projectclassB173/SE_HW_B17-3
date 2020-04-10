k = -9
if k>= 0:
    result = str(k) +"正数"
    print(result)
else:
    print(str(k)+ "负数")


# comments start
# 错误的地方：
# 2k = -9   变量名不能数字开头 改为k = -9
# if else的缩进  改为 和k = -9对齐
# if 2k>= 0  变量名不能数字开头 改为k>0
# with = 2k +"正数" 字符串不能和整形相加 改为result = str(k) +"正数"
# print(with) 缩进不对 改为和result = str(k) +"正数"一样的缩进
# print(with) 前面改成了result 所以改为print(result)
# print(2K+ '负数") 字符串不能和整形相加并且负数的引号错误并且k是小写 改为 print(str(k)+ "负数")
# comments end