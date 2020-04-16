#编写程序，计算百钱买百鸡问题。假设公鸡5元一只，母鸡3元一只，小鸡1元三只，现在有100块钱，想买100只鸡，问有多少种买法？
#根据方程式组x+y+z=100和5x+3y+(1/3)z=100，即15x+9b+c=300，得出公鸡，母鸡，小鸡的取值范围
count=0
for a in range(0,101):
    for b in range(0,101):
        for c in range(0,101):
            if a*5+b*3+c/3==100 and a+b+c==100:
                print("公鸡:",a,"母鸡:",b,"小鸡:",c)
                count = count + 1
                print('共有%d种买法' % count)