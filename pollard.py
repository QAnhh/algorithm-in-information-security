def gcd(a, b):
    if a == b:
        return 1
    while b > 0:
        r = a % b
        a = b
        b = r
    return a


def pollard(n):
    a = 2
    b = 2
    while 1:
        a = (a * a + 1) % n #5
        b = (b * b + 1) % n #5
        b = (b * b + 1) % n #25
        d = gcd(a-b, n)
        if 1 < d < n:
            return d
        if d == n:
            return "that bai"


def main():
    print("nhap n:", end = " ")
    n = int(input())
    print(pollard(n))


if __name__ == '__main__':
    main()
