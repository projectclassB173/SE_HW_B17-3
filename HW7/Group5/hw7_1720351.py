def gcd_yue(m, n, p=-1):  
    while m:
        p, m, n = m*n if p == -1 else p, n % m, m
    return (p // n,n)
print(gcd_yue(20, 30))

def count(s):
  print('英文字符数', len([i for i in s if i.isalpha()]), '数字字符数', len([i for i in s if i.isdigit()]), '空格字符数', len([i for i in s if i.isspace()]), '其他字符数', len([i for i in s if not (i.isspace() or i.isalpha() or i.isdigit())]))
count(input("请输入一个字符串："))
