a=0
for x in range(1,20):
     for y in range(1,34):          
          for z in range(1,100):
               if (5*x+3*y+z/3==100) and x+y+z==100:
                    a=a+1;
                         print("买法种类:",a,"公鸡:",x,"母鸡:",y,"小鸡:",z)