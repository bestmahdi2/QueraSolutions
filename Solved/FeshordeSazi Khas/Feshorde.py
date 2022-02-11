a = str(input())
def feshar(n):
    n = str(n)
    new = []
    shomaresh = ""
    string = ""
    for i in n:
        if i not in new:
            new.append(i)
    for j in new:
        string += (j)
        q = n.count(j)
        if q >= 2:
            shomaresh += str(q)
    res = string + shomaresh
    res = list(res)
    res.sort()
    p = ""
    for k in res:
        p += k
    return p
while True:
    w = feshar(a)
    if w == a:
        print(w)
        break
    else:
        a = w
