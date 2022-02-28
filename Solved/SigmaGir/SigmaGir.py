# سیگماگیر
# ID : 647
# https://quera.ir/problemset/university/647/%D8%B3%DB%8C%DA%AF%D9%85%D8%A7%DA%AF%DB%8C%D8%B1
# https://b2n.ir/r07366

n = int(input())
m = int(input())
i = -10
j = 1
hasel = 0

for item in range(i, m + 1):
    for item1 in range(j, n + 1):
        s = (item + item1) ** 3 / item1 ** 2
        hasel += int(s)

print(hasel)
