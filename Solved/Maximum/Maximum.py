# ماکزیمم
# 588
# https://quera.ir/problemset/university/588/%D8%B3%D8%A4%D8%A7%D9%84-%D8%AF%D8%A7%D9%86%D8%B4%DA%AF%D8%A7%D9%87-%D8%B5%D9%86%D8%B9%D8%AA%DB%8C-%D8%B4%D8%B1%DB%8C%D9%81-%D9%85%D8%A8%D8%A7%D9%86%DB%8C-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87%D9%86%D9%88%DB%8C%D8%B3%DB%8C-%D9%BE%D8%A7%DB%8C%DB%8C%D8%B2-%DB%B9%DB%B3-%D9%85%D8%A7%DA%A9%D8%B2%DB%8C%D9%85%D9%85
# https://b2n.ir/078066


n = int(input())
voroodi = input()
maximum = 0

voroodi = voroodi.split(" ")
for i in voroodi:
    if int(i) > maximum:
        maximum = int(i)
print(maximum)

###########################################################

n = int(input())
voroodi = input()

maximum = max(voroodi.split(" "))
print(maximum)

###########################################################

n = int(input())
voroodi = input()
maximum = 0

for i in voroodi:
    if " " not in voroodi:
        adad = int(voroodi)
    else:
        fasele = voroodi.index(" ")
        adad = int(voroodi[:fasele+1])
        voroodi = voroodi[fasele+1:]

    if adad > maximum:
        maximum = adad

