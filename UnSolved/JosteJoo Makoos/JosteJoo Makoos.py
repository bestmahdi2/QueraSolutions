# جستوجوی معکوس
# ID : 632
# https://quera.org/problemset/632/
# https://b2n.ir/s86937

import re

a = input()
b = input()


def count(tpye, find):
    tpye = (str(tpye).lower())
    a1 = len(re.findall(str(find).lower(), tpye))

    tpyec = find[::-1]
    a2 = len(re.findall(str(tpyec).lower(), tpye))

    print(a1 + a2)


count(a, b)
