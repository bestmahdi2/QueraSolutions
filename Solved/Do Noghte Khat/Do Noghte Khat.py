# دو نقطه خط
# ID : 3414
# https://quera.ir/problemset/contest/3414/%D8%B3%D8%A4%D8%A7%D9%84-%D8%AF%D9%88-%D9%86%D9%82%D8%B7%D9%87-%D8%AE%D8%B7
# https://b2n.ir/n47769

string = input().split()

if string[0] == string[2]:
    print("Vertical")

elif string[1] == string[3]:
    print("Horizontal")

else:
    print("Try again")
