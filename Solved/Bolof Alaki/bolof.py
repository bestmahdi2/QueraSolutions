import re
a = int(input())
n = 0
for i in range(a):
    b = input().replace(" ", "")
    c = input().replace(" ", "")
    if (re.match(b, c)) != True:
        q = len(b)
        q1 = len(c)
        if abs(q - q1) == 1:
            n += 1
print(n)
