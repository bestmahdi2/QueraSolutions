# مثلث خیام پاسکال
# ID : 3410
# https://quera.org/problemset/3410/
# https://b2n.ir/e61578

def printPascal(n):
    for line in range(0, n):
        for i in range(0, line + 1):
            print(binomialCoeff(line, i),
                  " ", end="")
        print()


def binomialCoeff(n, k):
    res = 1
    if (k > n - k):
        k = n - k
    for i in range(0, k):
        res = res * (n - i)
        res = res // (i + 1)
    return res


n = int(input())
printPascal(n)
