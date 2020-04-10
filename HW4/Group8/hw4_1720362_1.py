for x in range(21):                                                         # 公鸡定义变量为x，且最多为20只
   for y in range(34):                                                        # 母鸡定义变量为y，且最多为33只
         z = 100-x-y
         if (z%3==0 and 5*x + 3*y + z/3 == 100):                                     # 总共花费100元
            print(x,y,z)
