# مربع توخالی
# ID : 283
# https://quera.ir/problemset/university/283/%D8%B3%D8%A4%D8%A7%D9%84-%D8%AF%D8%A7%D9%86%D8%B4%DA%AF%D8%A7%D9%87-%D8%B5%D9%86%D8%B9%D8%AA%DB%8C-%D8%B4%D8%B1%DB%8C%D9%81-%D9%85%D8%A8%D8%A7%D9%86%DB%8C-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87%D9%86%D9%88%DB%8C%D8%B3%DB%8C-%D8%A8%D9%87%D8%A7%D8%B1-%DB%B9%DB%B4-%D9%85%D8%B1%D8%A8%D8%B9-%D8%AA%D9%88%D8%AE%D8%A7%D9%84%DB%8C
# https://b2n.ir/106578

a, b = int(input()), int(input())

if b >= a:
    print("Wrong order!")
elif (b-a) % 2 != 0:
    print("Wrong difference!")
else:
    c = a - b
    ro_zir = ("* " * a + "\n") * (c//2)
    vasat = ("* " * (c//2) + "  " * b + "* " * (c//2) + "\n") * b
    print(f'{ro_zir}{vasat}{ro_zir[:-1]}')

###########################################################

