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
