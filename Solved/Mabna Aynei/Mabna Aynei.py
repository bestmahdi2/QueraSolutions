# مبنای آینه ای
# ID : 651
# https://quera.org/problemset/651/
# https://b2n.ir/s19003

def val(c):
    if (c >= '0' and c <= '9'):
        return ord(c) - 48
    else:
        return ord(c) - 65 + 10


def toDeci(strr, base):
    lenn = len(strr)
    power = 1
    num = 0
    for i in range(lenn - 1, -1, -1):
        if (val(strr[i]) >= base):
            print("Invalid Number")
            return -1
        num += val(strr[i]) * power
        power = power * base

    return num


def reVal(num):
    if (num >= 0 and num <= 9):
        return chr(num + 48)
    else:
        return chr(num - 10 + 65)


def fromDeci(base, inputNum):
    res = ""
    while (inputNum > 0):
        res += reVal(inputNum % base)
        inputNum //= base
    res = res[::-1]
    return res


def convertBase(s, a, b):
    num = toDeci(s, a)
    ans = fromDeci(b, num)
    return (ans)


s = str(input())
a = int(input())
b = int(input())
qwert = convertBase(s, a, b)
qwert = str(qwert)
if (qwert) == qwert[::-1]:
    print("YES")
else:
    print("NO")
