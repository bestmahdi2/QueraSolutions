# سراب
# ID : 4067
# https://quera.ir/problemset/contest/4067/%D8%B3%D8%A4%D8%A7%D9%84-%D8%B3%D8%B1%D8%A7%D8%A8
# https://b2n.ir/a44383

t = int(input())
keeper = []

for i in range(t):
    keeper.append([int(i) for i in input().split()])

locs = [(0, 0)]
k = 1

for i in range(1, 15000):
    if i % 2 != 0:
        locs.append((locs[i - 1][0] + 1, locs[i - 1][1] + 1))

    else:
        if k % 2 != 0:
            locs.append((locs[i - 1][0] + 1, locs[i - 1][1] - 1))

        else:
            locs.append((locs[i - 1][0] - 1, locs[i - 1][1] + 1))
        k += 1

for i in keeper:
    if (i[0], i[1]) in locs:
        print(locs.index(((i[0], i[1]))))

    else:
        print(-1)
