#鸡兔同笼问题。假设共有鸡、兔30只，脚90只，求鸡、兔各有多少只?

def main():
    for x in range(0, 45):
            y = 30 - x
            if 2 * x + 4 * y == 90:
                print('鸡: %d只, 兔: %d只' % (x, y))

if __name__ == '__main__':
    main()