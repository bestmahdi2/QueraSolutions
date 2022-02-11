# The Good, the Bad and the Ugly (1966)
# ID : 132247
# https://quera.org/problemset/132247/
# https://b2n.ir/m53931

from collections import Counter

a = int(input())
b = [input() for i in range(a)]
c = [input() for j in range(a - 1)]
d = c + b
x = Counter(d)

for u in d:
    if x[u] % 2 != 0:
        print(u)
        break