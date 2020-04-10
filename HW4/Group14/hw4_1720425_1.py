'''
1. 编写程序，计算百钱买百鸡问题。
假设公鸡5元一只，母鸡3元一只，小鸡1元三只，现在有100块钱，想买100只鸡，问有多少种买法？
'''
'''
解法：
设公鸡数为x，母鸡数为y，小鸡数为z
则可得
(1)x+y+z=100
(2)5x+3y+(1/3)z=100

同时，可知
x的范围为0<=x<=20，
y的范围为0<=y<=33，
z的范围为0<=z<=100。
'''


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
print("计算完成！")