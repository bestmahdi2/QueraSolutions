# ب.م.م و ک.م.م
# ID : 590
# https://quera.ir/problemset/university/590/%D8%B3%D8%A4%D8%A7%D9%84-%D8%AF%D8%A7%D9%86%D8%B4%DA%AF%D8%A7%D9%87-%D8%B5%D9%86%D8%B9%D8%AA%DB%8C-%D8%B4%D8%B1%DB%8C%D9%81-%D9%85%D8%A8%D8%A7%D9%86%DB%8C-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87%D9%86%D9%88%DB%8C%D8%B3%DB%8C-%D9%BE%D8%A7%DB%8C%DB%8C%D8%B2-%DB%B9%DB%B3-%D8%A8%D9%85%D9%85-%D9%88-%DA%A9%D9%85%D9%85
# https://b2n.ir/y24929


string = input()
n, m = sorted([int(i) for i in string.split(" ")])

n1, m1 = n, m
while m > 0:
    print(m, n)
    b = n % m
    n = m
    m = b
print(n, n1 * m1//n)

###########################################################

string = input()
n, m = sorted([int(i) for i in string.split(" ")])

from math import gcd
print(gcd(n, m), (n*m)//gcd(n, m))

###########################################################

string = input()
n, m = sorted([int(i) for i in string.split(" ")])

n1, m1 = n, m
while m:
    n, m = m, n % m
print(n, m1*n1//n)

###########################################################
# doesn't get 100 :

string = input()
n, m = sorted([int(i) for i in string.split(" ")])

bmm = 1
for i in range(m, 0, -1):
    if n % i == 0 and m % i == 0:
        bmm = i
        break
kmm = m
while True:
   if kmm % m == 0 and kmm % n == 0:
       break
   kmm += 1
print(bmm, kmm)
