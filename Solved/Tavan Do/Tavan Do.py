# توان دو
# ID : 616
# https://quera.ir/problemset/university/616/%D8%B3%D8%A4%D8%A7%D9%84-%D8%AF%D8%A7%D9%86%D8%B4%DA%AF%D8%A7%D9%87-%D8%B5%D9%86%D8%B9%D8%AA%DB%8C-%D8%B4%D8%B1%DB%8C%D9%81-%D9%85%D8%A8%D8%A7%D9%86%DB%8C-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87%D9%86%D9%88%DB%8C%D8%B3%DB%8C-%D9%BE%D8%A7%DB%8C%DB%8C%D8%B2-%DB%B9%DB%B3-%D8%AA%D9%88%D8%A7%D9%86-%D8%AF%D9%88
# https://b2n.ir/083186

n = int(input())
adad = 1

i = 0
j = 0
while i < n:
    while j < i:
        adad *= 2
        j += 1
    if n < adad:
        print(adad)
        break
    i += 1

###########################################################

n = int(input())
adad = 1

tedad = 0
baghi_mande = n
while True:
    tedad += 1
    baghi_mande /= 2
    if baghi_mande <= 1:
        break
for i in range(1, tedad + 1):
    adad *= 2
print(adad)

###########################################################

n = int(input())
adad = 1

for i in range(n):
    for j in range(i):
        adad *= 2
    if n < adad:
        print(adad)
        break
