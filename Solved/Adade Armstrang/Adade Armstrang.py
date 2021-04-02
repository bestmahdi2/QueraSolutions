# عدد آرمسترانگ
# ID : ---
#
#

n = input()

jame_argham = 0
x = 0
while x < len(n):
    jame_argham += int(n[x]) ** 3
    x += 1

if jame_argham == int(n):
    print("YES")
else:
    print("NO")


###########################################################

n = input()

adaad = [int(i) for i in n]
x = 0
jame_adaad = 0
while x < len(adaad):
    adaad[x] = adaad[x] ** 3
    x += 1
for i in adaad:
    jame_adaad += i
if jame_adaad == int(n):
    print("YES")
else:
    print("NO")

###########################################################

n = input()

adaad = [int(i) for i in n]
x = 0
while x < len(adaad):
    adaad[x] = adaad[x] ** 3
    x += 1

jame_adaad = sum(adaad)

if jame_adaad == int(n):
    print("YES")
else:
    print("NO")


###########################################################

n = input()

print("YES" if sum([int(i)**3 for i in n]) == int(n) else "NO")

###########################################################

n = input()

jame_argham = 0
for i in n:
    jame_argham += int(i) ** 3
if jame_argham != int(n):
    print("NO")
else:
    print("YES")
