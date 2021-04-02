# مجموع ارقام
# ID : ---
#
#

n = input()
adad = 0

x = len(n)-1
while 0 <= x:
    adad += int(n[x])
    x -= 1
print(adad)

###########################################################

n = input()
adad = 0

for i in range(len(n)):
    adad += int(n[i])

print(adad)

###########################################################

n = input()
adad = 0

x = 0
while x < len(n):
    adad += int(n[x])
    x += 1

print(adad)

###########################################################

n = input()

adad = sum([int(i) for i in n])

print(adad)

###########################################################

n = input()
adad = 0

for i in n:
    adad += int(i)

print(adad)
