# بدخواه پویان
# ID : 2705
# https://quera.ir/problemset/contest/2705/%D8%A8%D8%AF%D8%AE%D9%88%D8%A7%D9%87%20%D9%BE%D9%88%DB%8C%D8%A7%D9%86
# https://b2n.ir/q46709

p, d = [int(i) for i in input().split()]

x = 1
while True:
    if 0 <= (x * d) % p <= p / 2:
        print(x * d)
        break
    x += 1
