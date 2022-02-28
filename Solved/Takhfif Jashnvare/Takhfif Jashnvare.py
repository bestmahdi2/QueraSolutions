# تخفیف جشنواره
# ID : 44080
# https://quera.org/problemset/44080/
# https://b2n.ir/n59859

a, b = map(int, input().split())
c = list(map(int, input().split()))
c.sort()
s = 1

for i in range(len(c) - 1):
    if c[i] + c[i + 1] <= b and len(c) > 1:
        s += 1
    else:
        break

print(s)
