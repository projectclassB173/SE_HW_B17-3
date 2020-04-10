for i in range(0, 23):
    for j in range(0, 45):
        if (i + j == 30) and (i * 4 + j * 2 == 90):
            print('鸡：%s 只，兔：%s 只' % (j, i))