# Parquet (2020)
# ID : 132252
# https://quera.org/problemset/132252/
# https://b2n.ir/p04211

a,b = map(int, input().split())
z = (a + 4) // 2
g = a + b
delta = (z**2)-(4*g)

if delta > 0:
    x1 = ((-z) + (delta ** 0.5)) // (-2)
    x2 = ((-z) - (delta ** 0.5)) // (-2)
    y1 = (int(max(x1, x2)))
    y2 = (int(min(x2, x1)))
    print(y1, y2, sep=" ")

else:
    x1 = ((-z) // (-2))
    print(x1, x1, sep=" ")