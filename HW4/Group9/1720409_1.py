# 计算百钱买百鸡问题。假设公鸡5元一只，母鸡3元一只，小鸡1元三只，现在有100块钱，想买100只鸡，问有多少种买法？
a=0
for x in range(1,20):
     for y in range(1,34):
          for z in range(1,100):
               if (5*x+3*y+z/3==100) and x+y+z==100:
                 a=a+1;
                 print("买法:",a,"公鸡:",x,"母鸡:",y,"小鸡:",z)