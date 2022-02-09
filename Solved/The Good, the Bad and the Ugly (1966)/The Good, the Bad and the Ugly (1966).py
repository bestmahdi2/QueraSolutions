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
