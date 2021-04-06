# استارت-آپ باکلاس
# ID : 10326
# https://quera.ir/problemset/contest/10326/%D8%B3%D8%A4%D8%A7%D9%84-%D8%A7%D8%B3%D8%AA%D8%A7%D8%B1%D8%AA-%D8%A2%D9%BE-%D8%A8%D8%A7%DA%A9%D9%84%D8%A7%D8%B3
# https://b2n.ir/m53560

string = [int(i) for i in input().split()]

keeper = [0, 0, 0, 0]

person = 0
while True:
    if 0 in string:
        break

    string[person % 4] -= 1
    keeper[person % 4] += 1
    string.insert(3, string.pop(0))
    person += 1

print(" ".join([str(i) for i in keeper]))

###########################################################
