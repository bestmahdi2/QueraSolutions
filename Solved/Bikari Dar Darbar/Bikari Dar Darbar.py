# بیکاری در دربار
# ID : 8939
# https://quera.org/problemset/8939/
# https://b2n.ir/a16654


import re


def solve(n):
    n = str(n)
    b = n.split()
    b.remove("+")
    b.remove("=")
    o = 0
    for i in range(3):
        g = b[i].count("#")
        if g == 1:
            o += i
            break
    if o == 0:
        v = int(b[2]) - int(b[1])

    elif o == 1:
        v = int(b[2]) - int(b[0])

    else:
        v = int(b[0]) + int(b[1])

    v = str(v)
    an = b[o].replace("#", ".*")

    if re.match(rf'^{an}$', v):
        b[o] = v
        return (b[0] + " + " + b[1] + " = " + b[2])

    else:
        return -1


a = str(input())
print(solve(a))
