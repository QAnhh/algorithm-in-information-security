import math


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    else:
        while b > 0:
            r = a % b
            a = b
            b = r
    return a


def is_prime(n):
    if n < 2:
        return 0
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return 0
    return 1


def is_camichael(n):
    if is_prime(n) == 1 or n < 2:
        return 0
    for i in range(2, n):
        if gcd(i, n) == 1:
            if pow(i, n-1) % n != 1:
                return 0
    return 1


def main():
    print("nhap n: ", end = " ")
    n = int(input())
    for i in range(1, n+1, 2):
        if(is_camichael(i)):
            print(i, end = " ")


if __name__ == '__main__':
    main()
