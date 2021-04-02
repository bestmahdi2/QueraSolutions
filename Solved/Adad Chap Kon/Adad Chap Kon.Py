# عدد چاپ کن
# ID : 9774
# https://quera.ir/problemset/university/9774/%D8%B3%D8%A4%D8%A7%D9%84-%D8%AF%D8%A7%D9%86%D8%B4%DA%AF%D8%A7%D9%87-%D8%B5%D9%86%D8%B9%D8%AA%DB%8C-%D8%A7%D9%85%DB%8C%D8%B1%DA%A9%D8%A8%DB%8C%D8%B1-%D9%85%D8%A8%D8%A7%D9%86%DB%8C-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87%D9%86%D9%88%DB%8C%D8%B3%DB%8C-%D9%BE%D8%A7%DB%8C%DB%8C%D8%B2-%DB%B9%DB%B5-%D8%B9%D8%AF%D8%AF-%DA%86%D8%A7%D9%BE%DA%A9%D9%86
# https://b2n.ir/593554

string = input()

for i in string:
    print(f'{i}: {i*int(i)}')

###########################################################

string = input()

for i in string:
    print("{0}: {1}".format(i, i*int(i)))

###########################################################

string = input()

x = 0
while x < len(string):
    print("%s: %s" % (string[x], string[x] * int(string[x])))
    x += 1
