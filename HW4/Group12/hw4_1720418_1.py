x=0
for a in range(0,101):
    for b in range(0,101):
        for c in range(0,101):
            if a*5+b*3+c/3==100 and a+b+c==100:
                x+=1
                print("公鸡:",a,"母鸡:",b,"小鸡:",c)
                print("总共", x, "种")

