#计算百钱买百鸡问题。假设公鸡5元一只，母鸡3元一只，小鸡1元三只，现在有100块钱，想买100只鸡，问有多少种买法？

def main():
    for x in range(0, 20):
        for y in range(0, 33):
            z = 100 - x - y
            if 5 * x + 3 * y + z / 3 == 100:
                print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))

if __name__ == '__main__':
    main()