# اسم‌ها
# ID : 2529
# https://quera.ir/problemset/contest/2529/%D8%B3%D8%A4%D8%A7%D9%84-%D8%A7%D8%B3%D9%85%D9%87%D8%A7
# https://b2n.ir/q28319

n = int(input())

lister = []
for i in range(n):
    lister.append(input())

print(max([len(set(i)) for i in lister]))