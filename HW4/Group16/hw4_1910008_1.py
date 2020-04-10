flag = 0
for i in range(0, 20):
    for j in range(0, 33):
        k = 100 - i - j
        if (k % 3 == 0) and (5 * i + 3 * j + k / 3 == 100):
            print('公鸡：%s 母鸡：%s 小鸡：%s' % (i, j, k))
            flag = flag + 1
print('共有%d种买法' % flag)
