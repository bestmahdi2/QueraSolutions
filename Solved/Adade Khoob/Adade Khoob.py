# عدد خوب
# ID : 9774
# https://quera.ir/problemset/university/66861/%D8%B9%D8%AF%D8%AF%20%D8%AE%D9%88%D8%A8
# https://b2n.ir/p78407

k = int(input())
n = 1

keeper = 0
while True:
    number = sum([i for i in range(n)])
    keeper = len([i for i in range(1, number + 1) if number % i == 0])
    n += 1
    if keeper >= k:
        print(number)
        break

###########################################################

k, i, a, t = int(input()), 0, 1, 0
while True:
    i += a
    for b in range(1, i + 1):
        if i % b == 0:
            t += 1
    if t >= k:
        print(i)
        break
    else:
        t = 0
    a += 1
