# هم‌نهشتی اعداد
# ID : 592
# https://quera.ir/problemset/university/592/%D8%B3%D8%A4%D8%A7%D9%84-%D8%AF%D8%A7%D9%86%D8%B4%DA%AF%D8%A7%D9%87-%D8%B5%D9%86%D8%B9%D8%AA%DB%8C-%D8%B4%D8%B1%DB%8C%D9%81-%D9%85%D8%A8%D8%A7%D9%86%DB%8C-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87%D9%86%D9%88%DB%8C%D8%B3%DB%8C-%D9%BE%D8%A7%DB%8C%DB%8C%D8%B2-%DB%B9%DB%B3-%D9%87%D9%85%D9%86%D9%87%D8%B4%D8%AA%DB%8C-%D8%A7%D8%B9%D8%AF%D8%A7%D8%AF
# https://b2n.ir/295907

n = sorted([int(i) for i in (input()).split(" ")])
# hamneheshti = n[1] % n[0]
lister = []
for i in range(1, n[1] + 1):
    if n[1] % i == n[0] % i:
        lister.append(str(i))
print(" ".join(lister))
