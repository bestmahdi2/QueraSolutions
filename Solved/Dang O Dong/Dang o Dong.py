# دَنگ و دُنگ
# ID : 127290
# https://quera.org/problemset/127290/
# https://b2n.ir/j65197

a = int(input())
h = []

for i in range(a):
    b = input().split()
    q = int(b[0])
    q1 = int(b[1])
    q2 = int(b[2])
    q1 -= q2

    if q1 % q == 0 and (q1 / q != 0) and (q1 / q > 0):
        res = q1 // q

    elif q1 / q == 0:
        res = (-1)

    elif q1 % q != 0:
        res = -1

    elif q1 % q == 0 and (q1 / q < 0):
        res = -1

    h.append(res)

for j in range(len(h)):
    k = h[j]
    print(k)
