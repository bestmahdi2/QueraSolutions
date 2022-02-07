# کلید چراغ
# ID : 49028
# https://quera.ir/problemset/contest/49028/%DA%A9%D9%84%DB%8C%D8%AF%20%DA%86%D8%B1%D8%A7%D8%BA
# https://b2n.ir/080336

status = 0
n = int(input())
names = [input() for i in range(n)]

for i in range(0, n - 1):
    if names[i] != names[i + 1]:
        status += 1

print(status)
