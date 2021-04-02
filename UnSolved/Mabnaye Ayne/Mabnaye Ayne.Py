# مبنای آینه‌ای
# ID : 651
# https://quera.ir/problemset/university/651/%D8%B3%D8%A4%D8%A7%D9%84-%D8%AF%D8%A7%D9%86%D8%B4%DA%AF%D8%A7%D9%87-%D8%B5%D9%86%D8%B9%D8%AA%DB%8C-%D8%B4%D8%B1%DB%8C%D9%81-%D9%85%D8%A8%D8%A7%D9%86%DB%8C-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87%D9%86%D9%88%DB%8C%D8%B3%DB%8C-%D9%BE%D8%A7%DB%8C%DB%8C%D8%B2-%DB%B9%DB%B3-%D9%85%D8%A8%D9%86%D8%A7%DB%8C-%D8%A2%DB%8C%D9%86%D9%87%D8%A7%DB%8C
# https://b2n.ir/j40014

a, b, c = int(input()), int(input()), int(input())

def numberToBase(n, b):
    strings = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" #36 symbols

    if n == 0:
        return 0
    numbers = ""
    while n:
        numbers += strings[n % b]
        n //= b
    numbers = numbers[::-1]

    return "".join(numbers)

to_x = int(numberToBase(a, b))
n = str(numberToBase(c, to_x))
if n == n[::-1]:
    print("YES")
else:
    print("NO")


