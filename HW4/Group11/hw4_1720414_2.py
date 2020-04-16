chick = 0
rabbit = 0
while chick <= 30  and  rabbit <= 30:
    if chick + rabbit == 30:
        if chick + 2 * rabbit == 45:
            break
    chick += 1
    rabbit = 30 - chick
print("结果：鸡有"+ str(chick) +"只,兔有"+ str(rabbit) +"只\n")