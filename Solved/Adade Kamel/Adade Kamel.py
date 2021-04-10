# عدد کامل
# ID : ---
#
#

N = int(input())

jam = 0
x = 1
while x < N:
    if N % x == 0:
        jam += x
    x += 1
if jam != N:
    print("NO")
else:
    print("YES")

###########################################################

N = int(input())

maghsoomha = [i for i in range(1, N) if N%i == 0]
jam = 0
for j in maghsoomha:
    jam += j
print("YES" if jam == N else "NO")


###########################################################

N = int(input())

print("YES" if sum([i for i in range(1, N//2 + 1) if N%i == 0]) == N else "NO")

###########################################################

N = int(input())

jam = 0
for x in range(1, N//2 + 1):
    if N % x == 0:
        jam += x
if jam != N:
    print("NO")
else:
    print("YES")
