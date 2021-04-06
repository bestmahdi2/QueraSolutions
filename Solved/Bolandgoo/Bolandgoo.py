# بلندگو
# ID : 3430
# https://quera.ir/problemset/contest/3430/%D8%B3%D8%A4%D8%A7%D9%84-%D8%A8%D9%84%D9%86%D8%AF%DA%AF%D9%88
# https://b2n.ir/651861

string = input()
print(string)

for i in range(1, len(string)):
    print(string[i] * i + string[i:])
