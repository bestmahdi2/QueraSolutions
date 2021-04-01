# یافتن عدد اول
# ID : 593

n = input()
b = sum([int(i) for i in n])

x, keep = 0, 0
for i in range(int(n)+1, 30000000):
    for j in range(2, i//2+1):
        if i % j == 0:
            break
    else:
        keep = i
        x += 1
    # print(i, x, n, b)
    if x == b:
        break
print(keep)
