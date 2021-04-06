# گردو شکستم
# ID : 3540
# https://quera.ir/problemset/contest/3540/%D8%B3%D8%A4%D8%A7%D9%84-%D8%AC%D8%B3%D8%AA-%D9%88-%D8%AC%D9%88-%D8%B1%DB%8C%D8%A7%D8%B6%DB%8C%D8%A7%D8%AA-%DA%AF%D8%B1%D8%AF%D9%88-%D8%B4%DA%A9%D8%B3%D8%AA%D9%85
# https://b2n.ir/037440

n, x, y = [int(i) for i in input().split()]

xtime = n//x
ytime = n//y

for i in range(xtime):
    for j in range(ytime, -1, -1):
        if (i * x + j * y) == n:
            print(i, j)
            break
    else:
        continue
    break
else:
    print(-1)

###########################################################
