# فرزاد فیلم بین
# ID : 655
# https://quera.ir/problemset/university/655/%D8%B3%D8%A4%D8%A7%D9%84-%D8%AF%D8%A7%D9%86%D8%B4%DA%AF%D8%A7%D9%87-%D8%B5%D9%86%D8%B9%D8%AA%DB%8C-%D8%B4%D8%B1%DB%8C%D9%81-%D9%85%D8%A8%D8%A7%D9%86%DB%8C-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87%D9%86%D9%88%DB%8C%D8%B3%DB%8C-%D9%BE%D8%A7%DB%8C%DB%8C%D8%B2-%DB%B9%DB%B3-%D9%81%D8%B1%D8%B2%D8%A7%D8%AF-%D9%81%DB%8C%D9%84%D9%85%D8%A8%DB%8C%D9%86
# https://b2n.ir/t13786

n = int(input())

lister = []
for i in range(n):
    j = input()
    lister.append(j.title())
print("\n".join(lister))

###########################################################

n = int(input())

lister = []
x = 0
while x < n:
    j = input()
    lister.append(j.title())
    x += 1
string = ""
for i in lister:
    string = string + "\n" + i
print(string)
