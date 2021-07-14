# همایش زندگی بهتر
# ID : 10325
# https://quera.ir/problemset/contest/10325/%D8%B3%D8%A4%D8%A7%D9%84-%D9%87%D9%85%D8%A7%DB%8C%D8%B4-%D8%B2%D9%86%D8%AF%DA%AF%DB%8C-%D8%A8%D9%87%D8%AA%D8%B1
# https://b2n.ir/832593

i = [int(j) for j in input().split(" ")]
if i[1] <= 10:
    print(f'Right {11 - i[0]} {i[1]}')
else:
    print(f'Left {11 - i[0]} {21 - i[1]}')

###########################################################

string = input().split(" ")

numbers = []
for i in string:
    numbers.append(int(i))

if numbers[1] <= 10:
    print("Right %s %s" % (11 - numbers[0], numbers[1]))
else:
    print("Right %s %s" % (11 - numbers[0], 21 - numbers[1]))
