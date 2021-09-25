def nhanBinhPhuongCoLap(a, k, n):
    b = 1
    if k == 0:
        return b
    tmp = k
    binaryK = []
    while tmp > 0:
        binaryK.append(tmp % 2)
        tmp = int(tmp / 2)
    if binaryK[0] == 1:
        b = a  #b = b*a
    for i in range(1, len(binaryK)):
        a = (a*a) % n
        if binaryK[i] == 1:
            b = (a*b) % n
    return b


def fermat(n):
    print("nhap so lan thu:", end = " ")
    t = int(input())
    for i in range(0, t):
        a = 2
        # r = pow(a, n-1) % n
        r = nhanBinhPhuongCoLap(a, n-1, n)
        if r != 1:
            return "hop so"
        a += 1
    return "nguyen to"


def main():
    print("nhap n:", end = " ")
    n = int(input())
    print(fermat(n))


if __name__ == '__main__':
    main()
