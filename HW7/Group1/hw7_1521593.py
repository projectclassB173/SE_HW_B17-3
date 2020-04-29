#1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
def common(a,b):
    c=a*b
    while(b!=0):
        temp=a%b
        a=b
        b=temp
    return (a,c//a)
print(common(7,8))

#2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。
def count(s):
    dig_num=0  #数字计数
    spa_num=0  #空格计数
    alp_num=0  #字母计数
    oth_num=0  #其他计数
    for i in s:
        if i.isdigit():
            dig_num+=1
        elif i.isspace():
            spa_num+=1
        elif i.isalpha():
            alp_num+=1
        else:
            oth_num+=1
    return (dig_num,alp_num,spa_num,oth_num)
res=count('dsd1 2@ #de4')
print(res)
