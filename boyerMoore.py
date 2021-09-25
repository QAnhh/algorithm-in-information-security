def L(p, x):
    for i in range(len(p)-1, -1, -1):
        if p[i] == x:
            return i
    return -1


def boyerMoore(T, p):
    m = len(p)
    i = m-1
    j = m-1
    while i < len(T):
        if T[i] != p[j]:
            min = j if j<(1+L(p, T[i])) else (1+L(p, T[i]))
            i = i + m - min
            j = m-1
        else:
            if j == 0:
                return i
            j -= 1
            i -= 1
    return -1


def main():
    T = 'abacaabadcaaaabbaabb'
    p = 'aaaa'
    # print("nhap chuoi T:", end = " ")
    # T = input()
    # print("nhap chuoi p:", end = " ")
    # p = input()
    print("vi tri cua chuoi p:", end = " ")
    print(boyerMoore(T, p))
    

if __name__ == '__main__':
    main()
