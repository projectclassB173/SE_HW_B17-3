count = 0
for i in range( 1,100):
    for j in range( 1,100):
        k = 100 - i -j 
        if  i*5 + j*3 + (100-i-j)*1/3 == 100:
            print("公鸡：",i,"只，母鸡：",j,"只，小鸡",k,"只")
        count ++

 print(count）