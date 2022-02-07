# فاکتوریل
# ID : 589
# https://quera.ir/problemset/university/589/%D8%B3%D8%A4%D8%A7%D9%84-%D8%AF%D8%A7%D9%86%D8%B4%DA%AF%D8%A7%D9%87-%D8%B5%D9%86%D8%B9%D8%AA%DB%8C-%D8%B4%D8%B1%DB%8C%D9%81-%D9%85%D8%A8%D8%A7%D9%86%DB%8C-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87%D9%86%D9%88%DB%8C%D8%B3%DB%8C-%D9%BE%D8%A7%DB%8C%DB%8C%D8%B2-%DB%B9%DB%B3-%D9%81%D8%A7%DA%A9%D8%AA%D9%88%D8%B1%DB%8C%D9%84
# https://b2n.ir/983182

n = int(input())
hasel = 1

for i in range(1, n + 1):
    hasel = hasel * i

print(hasel)

###########################################################

n = int(input())
hasel = 1

x = 1
while x <= n:
    hasel *= x
    x += 1

print(hasel)

###########################################################

n = int(input())
hasel = 1

x = 1
while x < n + 1:
    hasel = hasel * x
    x += 1
print(hasel)

###########################################################

n = int(input())
hasel = 1

x = 1
while x < n + 1:
    hasel *= x
    x += 1
print(hasel)

###########################################################

n = int(input())
hasel = 1

x = n
while 0 < x:
    hasel *= x
    x -= 1
print(hasel)

###########################################################

n = int(input())
hasel = 1

for j in range(n, 1, -1):
    hasel = hasel * j
print(hasel)
