def nhanBinhPhuongCoLap(a, k, n):
    b = 1
    if k == 0:
        return b
    binaryK = []
    tmp = k
    while tmp > 0:
        binaryK.append(int(tmp%2))
        tmp = int(tmp/2)
    if binaryK[0] == 1:
        b = a
    for i in range(1,len(binaryK)):
        a = (a*a) % n
        if binaryK[i] == 1:
            b = (a*b) % n
    return b


def millerRabin(n):
    s = 0
    r = n-1
    while r % 2 == 0:
        r /= 2
        s += 1
    print("nhap so lan thu:", end = " ")
    t = int(input())
    for i in range(0, t):
        a = 2
        y = nhanBinhPhuongCoLap(a, r, n)
        if y != 1 and y != n-1:
            j = 1
            while j <= s-1 and y != n-1:
                y = y*y % n
                if y == 1:
                    return "hop so"
                j += 1
            if y != n-1:
                return "hop so"
    return "nguyen to"


def main():
    print("nhap n:", end = " ")
    n = int(input())
    print(millerRabin(n))


if __name__ == '__main__':
    main()
