# فرزاد کارکن
# ID : 658
# https://quera.org/problemset/658/
# https://b2n.ir/m57632

import numpy

a = int(input())
b = [int(t) for t in input().split()]

if max(b) <= 0:
    print(0)

else:
    h = [max(b)]

    for i in range(2, a):
        for j in range(0, (a - (i)) + 1):
            h.append(numpy.sum([b[k] for k in range(j, j + i)]))

    print(max(h))
