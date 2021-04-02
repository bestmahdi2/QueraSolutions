# مجموع اعداد
# ID : ---
#
#

voroodi = input()
fard = 0
zoj = 0

voroodi = voroodi.split(" ")
x = 0
while x < len(voroodi):
    if int(voroodi[x]) % 2 == 0:
        zoj += int(voroodi[x])
    else:
        fard += int(voroodi[x])
    x += 1

print(zoj, fard)

###########################################################

voroodi = input()
fard = 0
zoj = 0

voroodi = voroodi.split(" ")
for i in voroodi:
    if int(i) % 2 == 0:
        zoj += int(i)
    else:
        fard += int(i)

print(zoj, fard)

###########################################################

voroodi = input()
fard = 0
zoj = 0

for i in range(6):
    if " " not in voroodi:
        adad = int(voroodi)
    else:
        fasele_char = voroodi.index(" ")
        adad = int(voroodi[:fasele_char + 1])
        voroodi = voroodi[fasele_char + 1:]

    if adad % 2 != 0:
        fard += adad
    else:
        zoj += adad

print(zoj, fard)
