# یافتن عدد اول
# ID : 593
# https://quera.ir/problemset/university/593/%D8%B3%D8%A4%D8%A7%D9%84-%D8%AF%D8%A7%D9%86%D8%B4%DA%AF%D8%A7%D9%87-%D8%B5%D9%86%D8%B9%D8%AA%DB%8C-%D8%B4%D8%B1%DB%8C%D9%81-%D9%85%D8%A8%D8%A7%D9%86%DB%8C-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87%D9%86%D9%88%DB%8C%D8%B3%DB%8C-%D9%BE%D8%A7%DB%8C%DB%8C%D8%B2-%DB%B9%DB%B3-%DB%8C%D8%A7%D9%81%D8%AA%D9%86-%D8%B9%D8%AF%D8%AF-%D8%A7%D9%88%D9%84
# https://b2n.ir/w97657

n = input()
b = sum([int(i) for i in n])

x, keep = 0, 0
for i in range(int(n) + 1, 30000000):
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            break
    else:
        keep = i
        x += 1
    if x == b:
        break
print(keep)

