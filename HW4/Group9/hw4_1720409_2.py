#鸡兔同笼问题:假设共有鸡、兔30只，脚90只，求鸡、兔各有多少只?
#设鸡有x只，兔有y只。根据方程式组x+y=30和2 * x + 4 * y == 90
for x in range(1,30):
    y = 30 - x
    if 2 * x + 4 * y == 90:
        print("鸡有", x,  "只。")
        print("兔有", y,  "只。")
