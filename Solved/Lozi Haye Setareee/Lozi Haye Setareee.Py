# لوزی های ستاره ای
# ID : 9773
# https://quera.ir/problemset/university/9773/%D8%B3%D8%A4%D8%A7%D9%84-%D8%AF%D8%A7%D9%86%D8%B4%DA%AF%D8%A7%D9%87-%D8%B5%D9%86%D8%B9%D8%AA%DB%8C-%D8%A7%D9%85%DB%8C%D8%B1%DA%A9%D8%A8%DB%8C%D8%B1-%D9%85%D8%A8%D8%A7%D9%86%DB%8C-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87%D9%86%D9%88%DB%8C%D8%B3%DB%8C-%D9%BE%D8%A7%DB%8C%DB%8C%D8%B2-%DB%B9%DB%B5-%D9%84%D9%88%D8%B2%DB%8C%D9%87%D8%A7%DB%8C-%D8%B3%D8%AA%D8%A7%D8%B1%D9%87%D8%A7%DB%8C
# https://b2n.ir/y21327

n = int(input())

for i in range(1, n + 1, 2):
    print(f'{" " * ((n - i) // 2)}{"*" * i}{" " * (n - i -1)}{"*" * i}')
for i in range(n-2, 0, -2):
    print(f'{" " * ((n - i) // 2)}{"*" * i}{" " * (n - i - 1)}{"*" * i}')

###########################################################

