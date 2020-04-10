#计算百钱买百鸡问题。假设公鸡5元一只，母鸡3元一只，小鸡1元三只，现在有100块钱，想买100只鸡，问有多少种买法？
#可得出公式x+y+z=100和5x+3y+(1/3)z=100，即15x+9b+c=300

plans = 0
for a in range(0,100):
    for b in range(0,100):
        c = 100 - a - b
        if c % 3 == 0 and 15 * a + 9 * b == 300 - c:
            print("公鸡:%d 母鸡:%d 小鸡:%d" % (a, b, c))
            plans = plans + 1
print('共有%d种方法' % plans)
