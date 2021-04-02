# خر در چمن فراوونه
# ID : 4065
# https://quera.ir/problemset/contest/4065/%D8%B3%D8%A4%D8%A7%D9%84-%D8%AE%D8%B1-%D8%AF%D8%B1-%DA%86%D9%85%D9%86-%D9%81%D8%B1%D8%A7%D9%88%D9%88%D9%86%D9%87
# https://b2n.ir/627599

number = (input()).split(" ")

a = int(number[0])
b = int(number[1])
l = int(number[2])

sums = 0

for i in range(1, l + 1):
    if i % 2 != 0:
        sums += a
    else:
        sums += b

print(sums)

###########################################################

number = (input()).split(" ")

a, b, l = int(number[0]), int(number[1]), int(number[2])

sums = 0
count = 1

while count <= l:
    if count % 2 != 0:
        sums += a
    else:
        sums += b
    count += 1

print(sums)


