import math


def chuyen_doi(x, w, t, res):
    for i in range(t-1, -1, -1):
        tmp = math.pow(2, i*w)
        res.append(math.floor(x/tmp))
        x = x % tmp


def phepNhan(a, b, t, w):
    c = [0]*2*t
    for i in range(0, len(a)):
        u = 0
        for j in range(0, len(b)):
            uv = c[i + j] + a[i]*b[j] + u
            u = int(uv/pow(2, w))
            v = uv % pow(2, w)
            c[i + j] = v
        c[i+t] = u
    c.reverse()
    print(c)
    return


def main():
    p = 2147483647
    w = 8
    m = math.ceil(math.log(p, 2))
    t = math.ceil(m / w)
    # a = [0]*t
    # b = [0]*t
    # print("nhap mang a:")
    # for i in range(0,len(a)):
    #     a[i] = int(input())
    # print("nhap mang b:")
    # for i in range(0, len(b)):
    #     b[i] = int(input())
    a = 524647
    b = 32549
    array_a = []
    array_b = []
    chuyen_doi(a, w ,t ,array_a)
    chuyen_doi(b, w ,t ,array_b)
    array_a.reverse()
    array_b.reverse()
    print(array_a, array_b)
    phepNhan(array_a, array_b, t, w)


if __name__ == '__main__':
    main()
