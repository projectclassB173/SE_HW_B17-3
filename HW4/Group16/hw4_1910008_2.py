for i in range(0, 25):
    for j in range(0, 50):
        if (i + j == 30) and (i * 4 + j * 2 == 90):
            print('鸡：%s 兔：%s' % (j, i))
