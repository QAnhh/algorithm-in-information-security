def nghichDao(u, v, p):
    x1 = 1
    x2 = 0
    while u != 1:
        q = int(v/u)
        r = v % u
        x = x2 - x1*q
        v = u
        u = r
        x2 = x1
        x1 = x
    x1 = x1 % p #khử số âm
    print("nghich dao:",x1)


def main():
    # a = 45682375
    # p = 489573857
    print("nhap a:")
    a = int(input())
    print("nhap p:")
    p = int(input())
    nghichDao(a, p, p)


if __name__ == '__main__':
    main()
