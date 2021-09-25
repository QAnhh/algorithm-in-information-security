def vet_can(p, t):
    j = 0
    count = 0
    for i in range(0, len(t)):
        if i - j + len(p) > len(t):
            break
        count += 1
        if t[i] == p[j]:
            while 1:
                count += 1
                j += 1
                i += 1
                if t[i] == p[j]:
                    if j == len(p)-1:
                        return i-j
                else:
                    j = 0
                    break
    return -1


def main():
    p = input()
    t = input()
    print(vet_can(p, t))


if __name__ == '__main__':
    main()