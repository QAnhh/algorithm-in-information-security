import math


def tru(a, b, w, c):
    e = 0
    for i in range(len(a)-1, -1, -1):
        c[i] = a[i] - b[i] - e
        if c[i] < 0:
            e = 1
            c[i] = c[i] % pow(2, w)
        else:
            e = 0
    return e


def chuyenDoi(x, w, t, arr):
    for i in range(t-1,-1,-1):
        tmp = math.pow(2, i*w)
        arr.append(math.floor(x/tmp))
        x = x % tmp


def truFp(arra, arrb, t, w, arrc, arrp):
    e = tru(arra, arrb, w, arrc)
    if e == 1:
        e = 0
        for i in range(t-1, -1, -1):
            arrc[i] = arrc[i] + arrp[i] + e
            if arrc[i] >= pow(2, w):
                e = 1
                arrc[i] = arrc[i] % pow(2, w)
            else:
                e = 0
    print(arrc)


def main():
    p = 2147483647
    w = 8
    m = math.ceil(math.log(p, 2))
    t = math.ceil(m/w)
    # print("nhap a nguyen:")
    # a = int(input())
    # print("nhap b nguyen:")
    # b = int(input())
    a = 38762497
    b = 568424364
    resa = []
    resb = []
    arrp = []
    chuyenDoi(p, w, t, arrp)
    print(arrp)
    chuyenDoi(a, w, t, resa)
    print("A= ", resa)
    chuyenDoi(b, w, t, resb)
    print("B= ", resb)
    arrc = [0]*t
    truFp(resa, resb, t, w, arrc, arrp)


if __name__ == '__main__':
    main()
