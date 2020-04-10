'''
2.鸡兔同笼问题。
假设共有鸡、兔30只，脚90只，求鸡、兔各有多少只?
'''
'''
解法：
设鸡数量为x，兔数量为y
则可得
(1)x+y=30
(2)2x+4y=90

可使用numpy库来解该线性方程组
'''

import numpy as np
from numpy.linalg import solve
a=np.mat([[1,1],[2,4]])#系数矩阵
b=np.mat([30,90]).T    #常数项列矩阵
x=solve(a,b)           #方程组的解
print("鸡的数量为{}，兔的数量为{}".format(x[0], x[1]))