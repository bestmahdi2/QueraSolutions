# شطرنج حرفه‌ای
# ID : 2636
# https://quera.ir/problemset/contest/2636/%D8%B3%D8%A4%D8%A7%D9%84-%D8%B4%D8%B7%D8%B1%D9%86%D8%AC-%D8%AD%D8%B1%D9%81%D9%87%D8%A7%DB%8C
# https://b2n.ir/571633

string = input().split()
keeper = []

i = 0
while i < len(string):
    if i < 2:
        keeper.append(str(1 - int(string[i])))
    elif i < 5:
        keeper.append(str(2 - int(string[i])))
    else:
        keeper.append(str(8 - int(string[i])))
    i += 1
print(" ".join(keeper))
