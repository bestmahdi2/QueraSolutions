# میانگین اعداد
# ID : ---
#
#

voroodi = input()

voroodi = voroodi.replace(" EXIT", "")
voroodi = [int(i) for i in voroodi.split(" ")]
jam = sum(voroodi)
tedad = len(voroodi)

print(int(jam / tedad))

###########################################################

voroodi = input()

print(int(sum(list(map(int, voroodi.replace(" EXIT", "").split(" ")))) / len(
    list(map(int, voroodi.replace(" EXIT", "").split(" "))))))

###########################################################

voroodi = input()
jam = 0
tedad = 0

voroodi = voroodi[:voroodi.index(" EXIT")]
for i in voroodi:
    tedad += 1
    if " " in voroodi:
        fasele_char = voroodi.index(" ")
        adad = int(voroodi[:fasele_char + 1])
        voroodi = voroodi[fasele_char + 1:]
        jam += adad
    else:
        adad = int(voroodi)
        jam += adad
        break

print(int(jam / tedad))
