# بهمن مرگبار
# ID : 2436
# https://quera.org/problemset/2436/
# https://b2n.ir/s12860

def shomarande(num):
    res = []
    for j in range(0, (m * 2), 2):
        r = o[j + 1] * num
        res.append(o[j] + r)
    return max(res)


m, n = map(int, input().split())
o = list(map(int, input().split()))
l = list(map(int, input().split()))

result = ""
for i in l:
    result += str(shomarande(i))
    result += " "

print(result)
