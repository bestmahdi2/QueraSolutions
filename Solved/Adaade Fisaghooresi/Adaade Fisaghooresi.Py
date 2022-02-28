# عدد فیثاغورثی
# ID : 280
# https://quera.ir/problemset/university/280/%D8%B3%D8%A4%D8%A7%D9%84-%D8%AF%D8%A7%D9%86%D8%B4%DA%AF%D8%A7%D9%87-%D8%B5%D9%86%D8%B9%D8%AA%DB%8C-%D8%B4%D8%B1%DB%8C%D9%81-%D9%85%D8%A8%D8%A7%D9%86%DB%8C-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87%D9%86%D9%88%DB%8C%D8%B3%DB%8C-%D8%A8%D9%87%D8%A7%D8%B1-%DB%B9%DB%B4-%D8%A7%D8%B9%D8%AF%D8%A7%D8%AF-%D9%81%DB%8C%D8%AB%D8%A7%D8%BA%D9%88%D8%B1%D8%AB%DB%8C
# https://b2n.ir/496654

a, b, c = int(input()), int(input()), int(input())

if a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == b ** 2 + a ** 2:
    print("YES")
else:
    print("NO")
