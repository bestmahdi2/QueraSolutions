#ID : 609
#https://quera.org/problemset/609/

import itertools as it

n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

def SpiralMatrix(matrix, rows, cols):
    result = []
    chap = 0
    bala = 0
    rast = rows - 1
    paeen = cols - 1
    while chap < rast+1 and bala < paeen+1:
        i=chap
        while i < rast + 1:
            result.append(matrix[bala][i])
            i+=1
        i=bala + 1
        while i < paeen +1 :
            result.append(matrix[i][rast])
            i+=1
        if chap < rast and bala < paeen:
            i = rast - 1
            while i > chap - 1:
                result.append(matrix[paeen][i])
                i -=1
            i = paeen - 1
            while i > bala:
                result.append(matrix[i][chap])
                i -=1
        rast -= 1
        paeen -= 1
        chap += 1
        bala += 1

    return result
import math
def IsSquareRoot(n):
    if n == int(math.sqrt(n))**2:
        return True
    return False
count = 0 
result = SpiralMatrix(matrix, n,n)
acc = it.accumulate(result)
for item in acc:
    if IsSquareRoot(item):
        count += 1
print(count) 