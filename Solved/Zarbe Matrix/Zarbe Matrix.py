# ضرب ماتریس ها
# ID : 607
# https://quera.org/problemset/607/
# https://b2n.ir/d37143

satr_soton = input().split()
matrix1 = []
matrix2 = []
for i in range(int(satr_soton[0])):
    matrix1.append([int(i) for i in input().split()])
for i in range(int(satr_soton[1])):
    matrix2.append([int(i) for i in input().split()])

matrixF = []
for i in range(int(satr_soton[0])):
    matrixF.append([])
    keep = []
    for j in range(int(satr_soton[2])):
        keep.append(0)
    matrixF[i] = keep

for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            matrixF[i][j] += matrix1[i][k] * matrix2[k][j]

for r in matrixF:
    print(" ".join([str(i) for i in r]))
