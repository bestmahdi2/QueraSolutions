# Chaarshanbegaan at Cafebazaar
# ID : 26110
# https://quera.org/problemset/26110/
# https://b2n.ir/n47149

a = int(input())
j = 0

for i in range(a):
    n, m = input().split()
    d1 = (int(n) ** 2) + (int(m) ** 2)
    d = d1 ** 0.5

    if d <= 10:
        r = 10
    elif d <= 30:
        r = 9
    elif d <= 50:
        r = 8
    elif d <= 70:
        r = 7
    elif d <= 90:
        r = 6
    elif d <= 110:
        r = 5
    elif d <= 130:
        r = 4
    elif d <= 150:
        r = 3
    elif d <= 170:
        r = 2
    elif d <= 190:
        r = 1
    else:
        r = 0

    j += r

print(j)