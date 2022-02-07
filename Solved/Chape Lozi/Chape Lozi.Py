# چاپ لوزی
# ID : 618
# https://quera.ir/problemset/university/618/%D8%B3%D8%A4%D8%A7%D9%84-%D8%AF%D8%A7%D9%86%D8%B4%DA%AF%D8%A7%D9%87-%D8%B5%D9%86%D8%B9%D8%AA%DB%8C-%D8%B4%D8%B1%DB%8C%D9%81-%D9%85%D8%A8%D8%A7%D9%86%DB%8C-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87%D9%86%D9%88%DB%8C%D8%B3%DB%8C-%D9%BE%D8%A7%DB%8C%DB%8C%D8%B2-%DB%B9%DB%B3-%DA%86%D8%A7%D9%BE-%D9%84%D9%88%D8%B2%DB%8C
# https://b2n.ir/304206

n = int(input())

for i in range(1, 2 * n + 2, 2):
    print(f'{" " * ((2 * n + 1 - i) // 2)}{"*" * i}')
for i in range(2 * n - 1, 0, -2):
    print(f'{" " * ((2 * n + 1 - i) // 2)}{"*" * i}')

###########################################################

n = int(input())

for i in range(1, 2 * n + 2, 2):
    print("{0}{1}".format(" " * ((2 * n + 1 - i) // 2), "*" * i))
for i in range(2 * n - 1, 0, -2):
    print("{0}{1}".format(" " * ((2 * n + 1 - i) // 2), "*" * i))

###########################################################

n = int(input())

x = 1
while x < 2 * n + 2:
    print("{0}{1}".format(" " * ((2 * n + 1 - x) // 2), "*" * x))
    x += 2

x = 2 * n - 1
while x > 0:
    print("{0}{1}".format(" " * ((2 * n + 1 - x) // 2), "*" * x))
    x -= 2
