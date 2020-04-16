cocks = 0
hens = 0
chicks = 0
count = 0
for cocks in range(0,21):
    for hens in range(0,34):
        chicks = 100-cocks-hens
        if 5*cocks + 3*hens + (1/3)*chicks == 100:
            count+=1
            print("[{}] 公鸡{}只，母鸡{}只，小鸡{}只".format(count,cocks, hens, chicks))