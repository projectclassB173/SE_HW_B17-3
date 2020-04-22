"""题目为
2k = -9         #变量名不能以数字作为开头

  if 2k>= 0:    #if else语句的代码块中缩进空白数量要相同

    with = 2k +"正数"   #变量名不能使用特殊字符“with”，所以改为缩写w
                        #变量k的数据类型为int整型，无法与字符串相加

       print(with)

    else:

    print(2K+ '负数") #表示字符串前后引号要一致，K与k区分大小写不是同一变量
"""
#最终修改为
k = -9

if k >= 0:

     w = str(k) + "正数"

     print(w)
     
else:
     print(str(k)+ "负数")
