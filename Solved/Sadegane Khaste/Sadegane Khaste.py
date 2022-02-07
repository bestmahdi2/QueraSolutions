# صدگان خسته
# ID : 3406
# https://quera.ir/problemset/contest/3406/%D8%B3%D8%A4%D8%A7%D9%84-%D9%BE%DB%8C%D8%A7%D8%AF%D9%87-%D8%B3%D8%A7%D8%B2%DB%8C-%D8%B5%D8%AF%DA%AF%D8%A7%D9%86-%D8%AE%D8%B3%D8%AA%D9%87
# https://b2n.ir/957810

a = input()
b = input()

if a == b:
    print(a, "=", b)

elif int(a[::-1]) > int(b[::-1]):
    print(b, "<", a)

else:
    print(a, "<", b)
