﻿# 标识符不能以数字开头；、
# with为关键字，无法作为标识符
# 标识符大小写需一致
# int类型的变量无法直接与str类型的变量通过“+”相连
# 单引号和双引号要成对出现
# 段落缩进需保持一致
# 引号需前后匹配

k = -9
if k>= 0:
    w = str(k) +"正数"
    print(w)
else:
    print(str(k)+ '负数')
