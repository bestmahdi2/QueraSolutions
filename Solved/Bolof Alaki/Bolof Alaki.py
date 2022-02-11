# بولوف الکی!
# ID : 9595
# https://quera.org/problemset/9595/
# https://b2n.ir/q61394

import re

a = int(input())
n = 0

for i in range(a):
    b = input().replace(" ", "")
    c = input().replace(" ", "")

    if not re.match(b, c):
        q = len(b)
        q1 = len(c)
        if abs(q - q1) == 1:
            n += 1

print(n)