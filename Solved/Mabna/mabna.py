# مبنا
# ID : 594
# https://quera.org/problemset/594/
# https://b2n.ir/p14485

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


a, b = map(int, input().split())
c = (numberToBase(a, b))
sum1 = 0
sum2 = 0

for i in range(0, len(c), 2):
    sum1 += c[i]

for j in range(1, len(c), 2):
    sum2 += c[j]

if sum1 == sum2:
    print("Yes")

else:
    print("No")
