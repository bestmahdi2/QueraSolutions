# هم نهشتی اعداد
# ID : 592
# https://quera.org/problemset/592/
# https://b2n.ir/295907

n = sorted([int(i) for i in (input()).split(" ")])
# hamneheshti = n[1] % n[0]
lister = []

for i in range(1, n[1] + 1):
    if n[1] % i == n[0] % i:
        lister.append(str(i))

print(" ".join(lister))
