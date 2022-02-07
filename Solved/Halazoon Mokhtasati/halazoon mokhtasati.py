# حلزون مختصاتی
# ID : 597
# https://quera.org/problemset/597/
# https://b2n.ir/x14220

a = int(input())
m = 0
while a > 4:
    a -= 4
    m += 1

if a % 4 == 0:
    print(-m - 1, m + 1)

elif a == 1:
    print(-m, -m)

elif a == 2:
    print(m + 1, -m)

elif a == 3:
    print(m + 1, m + 1)
