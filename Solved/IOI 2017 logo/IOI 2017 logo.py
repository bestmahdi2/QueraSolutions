# IOI 2017 Logo
# ID : 6315
# https://quera.org/problemset/6315/
# https://b2n.ir/q75134

res = []
while True:
    a = int(input())
    if a != 0:
        dict_ID = {}
        dict_tie1 = {}
        dict_tie2 = {}
        dict_tie3 = {}
        for i in range(a):
            b = [int(k) for k in input().split()]
            for j in range(1, b[0] + 1):
                if b[j] not in dict_ID.keys():
                    dict_ID[b[j]] = 0
                    dict_tie1[b[j]] = 0
                    dict_tie2[b[j]] = 0
                    dict_tie3[b[j]] = 0
            for o in range(1, b[0] + 1):
                if o == 1:
                    dict_ID[b[o]] += 3
                    dict_tie1[b[o]] += 1
                elif o == 2:
                    dict_ID[b[o]] += 2
                    dict_tie2[b[o]] += 1
                else:
                    dict_ID[b[o]] += 1
                    dict_tie3[b[o]] += 1
        maxs = max(dict_ID.values())
        h = []
        for i in dict_ID:
            if dict_ID[i] == maxs:
                h.append(i)
        if len(h) == 1:
            res.append(h)
        else:
            h1 = []
            for y1 in h:
                h1.append(dict_tie1[y1])
            r1 = []
            maxs = max(h1)
            for t1 in range(len(h1)):
                if h1[t1] == maxs:
                    r1.append(h[t1])
            if len(r1) == 1:
                res.append(r1)
            else:
                h2 = []
                for y2 in r1:
                    h2.append(dict_tie2[y2])
                r2 = []
                maxs2 = max(h2)
                for t2 in range(len(h2)):
                    if h2[t2] == maxs2:
                        r2.append(r1[t2])
                if len(r2) == 1:
                    res.append(r2)
                else:
                    h3 = []
                    for y3 in r2:
                        h3.append(dict_tie3[y3])
                    r3 = []
                    maxs3 = max(h3)
                    for t3 in range(len(h3)):
                        if h3[t3] == maxs3:
                            r3.append(r2[t3])
                    if len(r3) == 1:
                        res.append(r3)
                    else:
                        r3.sort()
                        res.append(r3)
    else:
        break

for e in res:
    for e2 in e:
        print(e2, end=" ")
    print()
# 4
# 3 5 2 1
# 3 12 5 2
# 2 1 2
# 3 2 1 5
# 2
# 3 3 2 1
# 2 2 3 1
