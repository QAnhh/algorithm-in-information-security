import math


def chuyen_doi(x, w, t, res):
    for i in range(t-1, -1, -1):
        tmp = math.pow(2, i*w)
        res.append(math.floor(x/tmp))
        x = x % tmp


def cong(a, b, w, c):
    e = 0
    for i in range(len(a)-1, -1, -1):
        c[i] = a[i] + b[i] + e
        if c[i] >= pow(2, w):
            e = 1
            c[i] = c[i] % pow(2, w)
        else:
            e = 0
    return e


def tru(a, b, w, res):
    e = 0
    for i in range(len(a) - 1, -1, -1):
        res[i] = a[i] - b[i] - e
        if res[i] < 0:
            e = 1
            res[i] = res[i] % pow(2, w)
        else:
            e = 0
    return e


def congFp(a, b, w, t, c, p):
    res = [0] * t
    e = cong(a, b, w, c)
    if e == 1 or c > p:
        e = tru(c, p, w, res)
    else:
        res = c
    print(e, res)


def main():
    p = 2147483647
    w = 8
    m = math.ceil(math.log(p, 2))
    t = math.ceil(m / w)
    array_p = []
    chuyen_doi(p, w, t, array_p)
    a = 2147483646
    b = 2147483643
    array_a = []
    array_b = []
    chuyen_doi(a, w, t, array_a)
    chuyen_doi(b, w, t, array_b)
    array_c = [0] * t
    congFp(array_a, array_b, w, t, array_c, array_p)


if __name__ == '__main__':
    main()
