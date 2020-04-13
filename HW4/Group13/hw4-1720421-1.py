a=0
for b in range(0,100):
    for c in range(0,100):
        d=100-b-c
        if d%3==0 and 15*b+9*c==300-d:
            print("公鸡:%d 母鸡:%d 小鸡:%d" %(b,c,d))
            a=a+1
print(a)