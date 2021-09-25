import math


def chuyen_doi(a, w, t, res):
    for i in range(t-1, -1, -1):
        tmp = math.pow(2, i*w)
        res.append(math.floor(a/tmp))
        a = a % tmp
    return


def main():
    p = int(input())
    w = int(input())
    m = math.ceil(math.log(p, 2))
    t = math.ceil(m / w)
    # print("nhap a:",end=" ")
    a = int(input())
    res = []
    chuyen_doi(a, w, t, res)
    print("A= [",end ="")
    print(res[0],end = "") 
    for i in range(1,len(res)):
        print("   %3d" %(res[i]),end = "")  
    print("]")
    # print("ket qua:")
    # print(res)
    return


if __name__ == '__main__':
    main()

