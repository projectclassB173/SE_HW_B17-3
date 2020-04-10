num=0
for x in range(1,20):
    for y in range(1,33):
        z=100-x-y
        if (5*x+3*y+z/3==100) and z%3==0:
            num+=1;
            print("第{0}种：公鸡{1}只，母鸡{2}只，小鸡{3}只".format(str(num),str(x),str(y),str(z)))