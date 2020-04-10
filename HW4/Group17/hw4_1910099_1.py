for a in range(0,101):
    for b in range(0,101):
        for c in range(0,101):
            if a*5+b*3+c/3==100 and a+b+c==100:
                print(a,b,c)
