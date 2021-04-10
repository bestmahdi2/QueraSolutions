# اعداد اول
# ID : 293
# https://quera.ir/problemset/university/293/%D8%B3%D8%A4%D8%A7%D9%84-%D8%AF%D8%A7%D9%86%D8%B4%DA%AF%D8%A7%D9%87-%D8%B5%D9%86%D8%B9%D8%AA%DB%8C-%D8%B4%D8%B1%DB%8C%D9%81-%D9%85%D8%A8%D8%A7%D9%86%DB%8C-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87%D9%86%D9%88%DB%8C%D8%B3%DB%8C-%D8%A8%D9%87%D8%A7%D8%B1-%DB%B9%DB%B4-%D8%A7%D8%B9%D8%AF%D8%A7%D8%AF-%D8%A7%D9%88%D9%84
# https://b2n.ir/844713

a = int(input())
b = int(input())

for i in range(a, b+1):
    adad_aval = True
    for x in range(2, i):
        if i % x == 0:
            adad_aval = False
            break
    if adad_aval == True:
        print(i)

###########################################################

a = int(input())
b = int(input())

for i in range(a, b+1):
    adad_aval = True
    for x in range(2, i):
        if i % x == 0:
            adad_aval = False
            break
    if adad_aval:
        if i != 1:
            print(i)


###########################################################

a = int(input())
b = int(input())

for i in range(a, b+1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        if i != 1:
            print(i)
