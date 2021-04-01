# مربع توخالی
# ID : 283

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
