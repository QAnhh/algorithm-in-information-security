def failure(p, F):
    F[0] = -1
    count = 0
    for j in range(2, len(p)):
        tienTo = 1
        hauTo = j-1
        while 1:
            if p[0:tienTo] == p[hauTo:j]: # so sánh giá trị đầu tiên của TT và HT
                count = tienTo          # nếu bằng thì set lại biến đếm = vị trí của tiền tố
            if hauTo == 1 or tienTo == j: # nếu 1 trong 2 vượt quá giới hạn thì đặt
                F[j] = count              # F[j] = count và break
                break
            tienTo += 1  #tăng độ dài tiên tố lên 1
            hauTo -= 1   #tương tự với hậu tố
        count = 0   #set lại giá trị biến đếm sau mỗi vòng lặp
    print(F)


def KMP(p, T, F):
    i = 0
    j = 0
    while i < len(T):
        if T[i] != p[j]:
            if j != 0:
                j = F[j] 
            else:
                i += 1
        else:
            if j == len(p)-1:
                return i-j
            i += 1
            j += 1
    return -1


def main():
    T = 'gatcgactacattattbcattcatcaaaaa'
    p = 'abaabb'
    # print("nhap chuoi T:", end = " ")
    # T = input()
    # print("nhap chuoi p:", end = " ")
    # p = input()
    F = [0]*len(p)
    failure(p, F)
    print("vi tri cua chuoi p:", end = " ")
    print(KMP(p, T, F))


if __name__ == '__main__':
    main()