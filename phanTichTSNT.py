def phanTichTSNT(n):
    count = 0
    coSo = []
    soMu = []
    i = 2
    while n > 1:
        while n%i == 0:
            count += 1
            n = int(n/i)
        if count > 0:
            coSo.append(i)
            soMu.append(count)
            count = 0
        i += 1
    print("coSo=", coSo, "soMu=",soMu)


def main():
    print("nhap n: ", end = " ")
    n = int(input())
    phanTichTSNT(n)


if __name__ == '__main__':
    main()
    