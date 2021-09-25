import math


def sangNguyenThuy (array):
    for i in range(2, len(array)):#2->n
        if array[i] == 1:
            print(i, end = " ")
            for j in range(2*i, len(array), i):#duyet boi cua i
                if array[j] == 1:
                    array[j] = 0


def main():
    print("nhap n:")
    n = int(input())
    a = [1]*(n+1)
    sangNguyenThuy(a)


if __name__ == '__main__':
    main()
