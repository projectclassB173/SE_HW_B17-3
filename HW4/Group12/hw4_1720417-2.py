#2.鸡兔同笼问题。假设共有鸡、兔30只，脚90只，求鸡、兔各有多少只?

for c in range(0,31):
     if 2*c+(30-c)*4 == 90:
	   print('鸡: %d只, 兔: %d只' % (c, 30-int(c)))