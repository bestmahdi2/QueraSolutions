# مجید و ماژیک هاش
# ID : 9109
# https://quera.org/problemset/9109/
# https://b2n.ir/t68946

a = int(input())
b = list(int(i) for i in input().split())
b.sort()
s = []

for j in b:
    if j not in s:
        s.append(j)

counter = b.count(s[0])

for k in range(1, len(s)):
    c = b.count(s[k])
    if c < counter:
        counter = c

for k2 in s:
    if b.count(k2) == counter:
        print(k2)
        break
