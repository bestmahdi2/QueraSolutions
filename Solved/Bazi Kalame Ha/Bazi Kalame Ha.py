# بازی کلمه‌ها
# ID : 87181
# https://quera.org/problemset/87181/
# https://b2n.ir/n48725

def words_check(s):
    s = str(s)
    q = s.split()
    res = ""
    dict = {}

    for i in range(len(q)):
        r = q[i]
        u = len(r)
        res1 = ""

        for j in range(len(r)):
            n = r[j].lower()
            if str(n).isalpha() == True:
                res1 += n

        if len(res1) > (u // 2):
            res += res1.capitalize()
            res += " "

    res2 = res.split()
    res3 = list(res2)

    for k in res3:
        dict[k] = res3.count(k)

    return (dict)
