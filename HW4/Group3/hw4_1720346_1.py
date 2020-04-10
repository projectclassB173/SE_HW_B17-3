count = 0
for i in range(0, 20):
    for j in range(0, 33):
        k = 100 - i - j
        if (k % 3 == 0) & (5 * i + 3 * j + k / 3 == 100):
            print('公鸡：%s 只，母鸡：%s 只，小鸡：%s 只' % (i, j, k))
            count = count + 1
print('---')
print('共有 %d 种买法' % count)
