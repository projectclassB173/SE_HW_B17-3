plans = 0
for a in range(0,100):
    for b in range(0,100):
        c = 100 - a - b
        if c % 3 == 0 and 15 * a + 9 * b == 300 - c:
            print("公鸡:%d 母鸡:%d 小鸡:%d" % (a, b, c))
            plans = plans + 1
print('共有%d种方法' % plans)