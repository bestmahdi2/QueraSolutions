dim = int(input())
mat_1 = []
for _ in range(dim):
    mat_1.append(list(map(int,input().split())))
mat_2 = []
for _ in range(dim):
    mat_2.append(list(map(int,input().split())))


result = list()
for i in range(dim):
   row = list()
   for j in range(dim):
      row.append(0)
   result.append(row)

for i in range(dim):
   for j in range(dim):
      for k in range(dim):
         result[i][j] += mat_1[i][k] * mat_2[k][j]

def minor_det(matrix,i,j):
    c = matrix

    c = c[:i] + c[i+1:]
    for k in range(len(c)):
        c[k] = c[k][:j] + c[k][j+1:]
    
    return c

def det(matrix ,n):
    if n == 1 :
        return matrix[0][0]
    if n == 2 :
        return matrix[0][0] * matrix[1][1] - matrix[0][1]*matrix[1][0]
    sum = 0
    for i in range(n):
        m = minor_det(matrix,0,i)
        sum += ((-1)**i) * matrix[0][i] * det(m,n-1)

    return sum

if det(result, dim)%2:
    print("Danial")
else:
    print("Farzad")