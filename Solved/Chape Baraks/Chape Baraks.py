# چاپ برعکس
# ID : 3405
# https://quera.ir/problemset/contest/3405/%D8%B3%D8%A4%D8%A7%D9%84-%DA%86%D8%A7%D9%BE-%D8%A8%D8%B1%D8%B9%DA%A9%D8%B3
# https://b2n.ir/637768

lister = []
while True:
    number = input()
    if number == "0":
        break
    lister.append(number)
for i in lister[::-1]:
    print(i)
