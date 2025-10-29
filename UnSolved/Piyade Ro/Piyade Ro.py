# پیاده رو
# ID : 104590
# https://quera.org/problemset/104590/
# https://b2n.ir/n02156

n,q = map(int, input().split())
a = list(map(int, input().split()))
b = [0]*n
j=0
for i in range(1,n):
    if a[i] != a[i-1]:
        b[i] = j
        b[i-1] = j
    else:
        j+=1
        b[i] = j
for _ in range(q):
    s,e = map(int, input().split())
    s,e = map(lambda x:x-1, (s,e))
    if b[s] == b[e]:
        print("YES")
    else:
        print("NO")
