# def gcd(a, b):
#     if b==0:
#         print('d=',a)
#     elif a == b:
#         print('d= 1')
#     else:
#         x2 = 1
#         x1 = 0
#         y2 = 0
#         y1 = 1
#         while b > 0:
#             q = int(a/b)
#             r = a % b
#             x = x2 - x1*q
#             y = y2 - y1*q
#             a = b
#             b = r
#             x2 = x1
#             x1 = x
#             y2 = y1
#             y1 = y
#         print('d=',a)

def gcd(a, b):
    if a == b:
        return 1
    while b > 0:
        r = a%b
        a = b
        b = r
    return a

def main():
    # a = 28150488
    # b = 10507620
    a = int(input())
    b = int(input())
    print('d=',gcd(a, b))


if __name__ == '__main__':
    main()
