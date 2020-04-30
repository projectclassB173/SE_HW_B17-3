'''
1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。
'''

#1
def cal_GCD_LCM(num1, num2):
    n1, n2 = num1, num2
    if n1 < n2:
        n1, n2 = n2, n1
    
    remainder = n1 % n2
    while remainder != 0:
        n1, n2 = n2, remainder
        remainder = n1 % n2
    
    GCD = n2
    LCM = int(num1*num2/GCD)
    return (GCD, LCM)

GCD_LCM = cal_GCD_LCM(15,25)
print("1、\n最大公约数：", GCD_LCM[0],"\n最小公倍数：", GCD_LCM[1], sep="")
print(GCD_LCM)
print(type(GCD_LCM))

print("---------------------------------------------")
#2
def cal_char_count(string):
    count_number = 0
    count_alpha = 0
    count_space = 0
    count_others = 0
    for character in string:
        if character.isdigit():
            count_number += 1
        if character.isalpha():
            count_alpha += 1
        if character.isspace():
            count_space += 1
    count_others = len(string) - count_number - count_alpha - count_space
    print("2、\n在该字符串中\n数字数量：", count_number, "\n字母数量：", count_alpha, "\n空格数量：", count_space, "\n其他数量：", count_others, sep="")

cal_char_count("This is a test of string for digit count, alphabet count, space count and other characters count!")