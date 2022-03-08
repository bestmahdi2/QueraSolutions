# پیاده رو
# ID : 104590
# https://quera.org/problemset/104590/
# https://b2n.ir/n02156

n, m = map(int, input().split())
h = [int(q) for q in input().split()]
res = []

for j in range(m):
    f = True
    n, k = map(int, input().split())

    if n < k:
        for i in range(n - 1, k - 1):
            if h[i] == h[i + 1]:
                res.append("NO")
                f = False
                break

        if f:
            res.append("YES")

    elif n > k:
        for i in range(n - 1, k - 1, -1):
            if h[i] == h[i - 1]:
                res.append("NO")
                f = False
                break

        if f:
            res.append("YES")

    else:
        res.append("NO")

print("\n".join(res))
