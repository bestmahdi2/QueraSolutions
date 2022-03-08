# ترمیم یک خاطره
# ID : 1364
# https://quera.org/problemset/1364/
# https://b2n.ir/b79174

import re

junk = int(input())
c = input()
b = c.split()
a = input().split()
res = []

for i in a:
    s = ""

    for j in i:
        if j.isalpha() == True:
            s += j
        else:
            s += "[a-z]"
    w = 0
    m = 0
    e = []

    for k in b:
        if re.match(rf"^{s}$", str(k)):
            e.append(k)
        else:
            w += 1

    if len(e) > 1:
        res.append("multiple")
        break

    elif w == junk:
        res.append("not recoverable")
        break

    else:
        res.append(e[0])

if "multiple" in res:
    print("multiple")

elif "not recoverable" in res:
    print("not recoverable")

else:
    print(*res)
