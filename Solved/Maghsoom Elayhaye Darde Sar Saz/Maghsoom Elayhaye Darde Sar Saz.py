# مقسوم‌علیه‌های دردسرساز
# ID : 33045
# https://quera.ir/problemset/contest/33045/%D8%B3%D8%A4%D8%A7%D9%84-%D8%B1%DB%8C%D8%A7%D8%B6%DB%8C%D8%A7%D8%AA-%D9%85%D9%82%D8%B3%D9%88%D9%85%D8%B9%D9%84%DB%8C%D9%87%D9%87%D8%A7%DB%8C-%D8%AF%D8%B1%D8%AF%D8%B3%D8%B1%D8%B3%D8%A7%D8%B2
# https://b2n.ir/g99973

n = int(input())
sum = 0
count = 0

for i in range(1, n + 1):
    for j in range(1, ((i + 1)//2 + 2)):
        if i % j == 0:
            sum += j
            count += 1
    if i > 3:
        sum += i
        count += 1
print(count, sum)
