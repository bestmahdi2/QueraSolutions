# بمب بازی
# ID : 3407
# https://quera.org/problemset/3407/
# https://b2n.ir/u03885

n, m = map(int, input().split())
d = int(input())
r = []

for x in range(n):
    r.append([])
    for y in range(m):
        r[x].append(0)

for i in range(d):
    b, c = map(int, input().split())
    r[b - 1][c - 1] = "*"

    if b != 1 and b != n and c != 1 and c != m:
        if r[b - 1][c - 2] != "*":
            r[b - 1][c - 2] += 1
        if r[b - 1][c] != "*":
            r[b - 1][c] += 1
        if r[b][c - 2] != "*":
            r[b][c - 2] += 1
        if r[b][c] != "*":
            r[b][c] += 1
        if r[b][c - 1] != "*":
            r[b][c - 1] += 1
        if r[b - 2][c] != "*":
            r[b - 2][c] += 1
        if r[b - 2][c - 1] != "*":
            r[b - 2][c - 1] += 1
        if r[b - 2][c - 2] != "*":
            r[b - 2][c - 2] += 1

    elif b == 1 and c != 1 and c != m:
        if r[b - 1][c - 2] != "*":
            r[b - 1][c - 2] += 1
        if r[b - 1][c] != "*":
            r[b - 1][c] += 1
        if r[b][c] != "*":
            r[b][c] += 1
        if r[b][c - 1] != "*":
            r[b][c - 1] += 1
        if r[b][c - 2] != "*":
            r[b][c - 2] += 1

    elif (b == 1 and c == 1):
        if r[b - 1][c] != "*":
            r[b - 1][c] += 1
        if r[b][c] != "*":
            r[b][c] += 1
        if r[b][c - 1] != "*":
            r[b][c - 1] += 1

    elif b == 1 and c == m:
        if r[b - 1][c - 2] != "*":
            r[b - 1][c - 2] += 1
        if r[b][c - 2] != "*":
            r[b][c - 2] += 1
        if r[b][c - 1] != "*":
            r[b][c - 1] += 1

    elif b == n and c != 1 and c != m:
        if r[b - 1][c - 2] != "*":
            r[b - 1][c - 2] += 1
        if r[b - 1][c] != "*":
            r[b - 1][c] += 1
        if r[b - 2][c] != "*":
            r[b - 2][c] += 1
        if r[b - 2][c - 1] != "*":
            r[b - 2][c - 1] += 1
        if r[b - 2][c - 2] != "*":
            r[b - 2][c - 2] += 1

    elif b == n and c == 1:
        if r[b - 1][c] != "*":
            r[b - 1][c] += 1
        if r[b - 2][c] != "*":
            r[b - 2][c] += 1
        if r[b - 2][c - 1] != "*":
            r[b - 2][c - 1] += 1

    elif b == n and c == m:
        if r[b - 1][c - 2] != "*":
            r[b - 1][c - 2] += 1
        if r[b - 2][c - 2] != "*":
            r[b - 2][c - 2] += 1
        if r[b - 2][c - 1] != "*":
            r[b - 2][c - 1] += 1

    elif c == 1:
        if r[b - 1][c] != "*":
            r[b - 1][c] += 1
        if r[b - 2][c] != "*":
            r[b - 2][c] += 1
        if r[b - 2][c - 1] != "*":
            r[b - 2][c - 1] += 1
        if r[b][c] != "*":
            r[b][c] += 1
        if r[b][c - 1] != "*":
            r[b][c - 1] += 1

    elif c == m:
        if r[b - 1][c - 2] != "*":
            r[b - 1][c - 2] += 1
        if r[b - 2][c - 2] != "*":
            r[b - 2][c - 2] += 1
        if r[b - 2][c - 1] != "*":
            r[b - 2][c - 1] += 1
        if r[b][c - 2] != "*":
            r[b][c - 2] += 1
        if r[b][c - 1] != "*":
            r[b][c - 1] += 1

for j in r:
    for u in j:
        print(u, end=" ")

    print()
