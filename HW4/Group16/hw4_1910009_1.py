x = 0 
y = 0
z = 0
count = 0

for x in range(0,101,3):
    for y in range(0,34,1):
        for z in range(0,21,1):
            if ((x + y + z) == 100 and (x + 9*y + 15*z) == 300):
                count = count + 1
print(count)