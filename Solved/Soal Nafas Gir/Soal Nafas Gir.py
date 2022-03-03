# سوال نفس گیر
# ID : 26651
# https://quera.org/problemset/26651/
# https://b2n.ir/u93919

a = int(input())
b = input().split()
c = input().split()
m = 0

for i in range(a):
    j = int(b[i]) * int(c[i])
    m += j

print(m)
