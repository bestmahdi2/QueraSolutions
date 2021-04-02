# تک رقمی
# ID : 3539
# https://quera.ir/problemset/contest/3539/%D8%B3%D8%A4%D8%A7%D9%84-%D8%AA%DA%A9%D8%B1%D9%82%D9%85%DB%8C
# https://b2n.ir/066773

i = input()
while len(i) > 1:
    i = str(sum([int(j) for j in i]))
print(int(i))

###########################################################

i = input()
while len(i) > 1:
    sum = 0
    for j in i:
        sum += int(j)
    i = str(sum)

print(int(i))
