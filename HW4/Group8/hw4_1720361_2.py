鸡兔同笼问题。假设共有鸡、兔30只，脚90只，求鸡、兔各有多少只?

for x in range(0,30):                                 #鸡定义变量为x，最多为30只
    y=30-x                                 #兔定义变量为y
    z=2*x                               #定义鸡脚的数量为z
    a=4*y                               #定义兔脚的数量为y

    if(z+a==90):                                 #若鸡腿和兔腿相加满足90的条件则输出
        print("鸡:"+str(x)+" 兔:"+str(y))