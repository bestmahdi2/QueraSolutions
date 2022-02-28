# مثلث خیام
# ID : 595
# https://quera.ir/problemset/university/595/%D8%B3%D8%A4%D8%A7%D9%84-%D8%AF%D8%A7%D9%86%D8%B4%DA%AF%D8%A7%D9%87-%D8%B5%D9%86%D8%B9%D8%AA%DB%8C-%D8%B4%D8%B1%DB%8C%D9%81-%D9%85%D8%A8%D8%A7%D9%86%DB%8C-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87%D9%86%D9%88%DB%8C%D8%B3%DB%8C-%D9%BE%D8%A7%DB%8C%DB%8C%D8%B2-%DB%B9%DB%B3-%D9%85%D8%AB%D9%84%D8%AB-%D8%AE%DB%8C%D8%A7%D9%85
# https://b2n.ir/w17445

n = int(input())
listCount = []
for i in range(1, n + 1):
    listCount.append([None for i in range(i)])

for i in range(n):
    listCount[i][0] = "1"
    listCount[i][len(listCount[i]) - 1] = "1"

for y in range(n):
    for x in range(len(listCount[y]) - 1):
        if listCount[y][x] is None:
            listCount[y][x] = str(int(listCount[y - 1][x - 1]) + int(listCount[y - 1][x]))

for numbers in listCount:
    print(" ".join(numbers))
