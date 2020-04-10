# 计算百钱买百鸡问题。假设公鸡5元一只，母鸡3元一只，小鸡1元三只，现在有100块钱，想买100只鸡，问有多少种买法？
for a in range(0, 101):
    for b in range(0, 101):
        for c in range(0, 101):
            if a*5+b*3+c/3 == 100 and a+b+c == 100:
                print("公鸡:%d 母鸡:%d 小鸡:%d" % (a, b, c))