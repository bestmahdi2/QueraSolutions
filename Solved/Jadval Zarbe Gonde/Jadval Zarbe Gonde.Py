# جدول ضرب گنده
# ID : 3409
# https://quera.ir/problemset/contest/3409/%D8%B3%D8%A4%D8%A7%D9%84-%D8%AC%D8%AF%D9%88%D9%84-%D8%B6%D8%B1%D8%A8-%DA%AF%D9%86%D8%AF%D9%87
# https://b2n.ir/608271

n = int(input())

for i in range(1, n+1):
    for j in range(1, n+1):
        print(i*j, end=" ")
    print()

###########################################################

n = int(input())
i = 1
while i < n + 1:
    j = 1
    while j < n + 1:
        print(i*j, end=" ")
        j += 1
    print()
    i += 1
