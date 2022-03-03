# ICPC
# ID : 26109
# https://quera.org/problemset/26109/
# https://b2n.ir/u33963

p1, s1 = map(int, input().split())
s2, p2 = map(int, input().split())
a = p1 + p2
b = s1 + s2

if a > b:
    print("Persepolis")

elif b > a:
    print("Esteghlal")

elif a == b:
    if s1 > p2:
        print("Esteghlal")

    elif p2 > s1:
        print("Persepolis")

    else:
        print("Penalty")
