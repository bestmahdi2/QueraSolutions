# فرزاد کارکن
# ID : 658
# https://quera.ir/problemset/university/658/%D8%B3%D8%A4%D8%A7%D9%84-%D8%AF%D8%A7%D9%86%D8%B4%DA%AF%D8%A7%D9%87-%D8%B5%D9%86%D8%B9%D8%AA%DB%8C-%D8%B4%D8%B1%DB%8C%D9%81-%D9%85%D8%A8%D8%A7%D9%86%DB%8C-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87%D9%86%D9%88%DB%8C%D8%B3%DB%8C-%D9%BE%D8%A7%DB%8C%DB%8C%D8%B2-%DB%B9%DB%B3-%D9%81%D8%B1%D8%B2%D8%A7%D8%AF-%DA%A9%D8%A7%D8%B1%DA%A9%D9%86
# https://b2n.ir/s16305

a, string = input(), (input()).split(" ")
string = [int(i) for i in string]
print(sum(string) if sum(string) > 1 else 0)