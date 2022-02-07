# معادله درجه دو
# ID : 294
# https://quera.ir/problemset/university/294/%D9%85%D8%B9%D8%A7%D8%AF%D9%84%D9%87%20%D8%AF%D8%B1%D8%AC%D9%87%20%D8%AF%D9%88
# https://b2n.ir/p13657

a = float(input())
b = float(input())
c = float(input())

delta = (b ** 2 - 4 * a * c)
if a != 0:
    if delta == 0:
        javab = (-b) / (2 * a)
        print(javab)
    elif delta > 0:
        javab1 = (-b + (delta ** 0.5)) / (2 * a)
        javab2 = (-b - (delta ** 0.5)) / (2 * a)
        print("%.3f\n%.3f" % (javab1, javab2) if javab1 < javab2 else "%.3f\n%.3f" % (javab2, javab1))
    else:
        print("IMPOSSIBLE")

else:
    if b != 0:
        print("%.3f" % (-c / b))
    else:
        print("IMPOSSIBLE")

###########################################################

a = float(input())
b = float(input())
c = float(input())

if (a, b) == (0, 0):
    print('IMPOSIBLE')

elif a == 0:
    print('{:0.3f}'.format(-c / b))

elif b ** 2 - (4 * a * c) < 0:
    print('IMPOSIBLE')

elif b ** 2 - (4 * a * c) == 0:
    print('{:0.3f}'.format((-b + (b ** 2 - (4 * a * c)) ** 0.5) / (2 * a)))

else:
    javab1 = (-b + (b ** 2 - (4 * a * c)) ** 0.5) / (2 * a)
    javab2 = (-b - (b ** 2 - (4 * a * c)) ** 0.5) / (2 * a)
    if javab1 > javab2:
        print('{:0.3f}'.format(javab2));
        print('{:0.3f}'.format(javab1))
    else:
        print('{:0.3f}'.format(javab1));
        print('{:0.3f}'.format(javab2))

###########################################################

a = float(input())
b = float(input())
c = float(input())

delta = (b ** 2 - 4 * a * c)

if a != 0:
    if delta == 0:
        x = (-b) / (2 * a)
        x_string = str(x) + "000"
        int_string = str(int(x)) if x >= 0 else "-" + str(int(x))
        x = int_string + (x_string[x_string.index("."):x_string.index(".") + 4])
        print(x)
    elif delta > 0:
        x1 = (-b + (delta ** 0.5)) / (2 * a)
        x1_string = str(x1) + "000"
        int_string1 = str(int(x1)) if x1 >= 0 else "-" + str(int(x1))
        x1 = int_string1 + (x1_string[x1_string.index("."):x1_string.index(".") + 4])

        x2 = (-b - (delta ** 0.5)) / (2 * a)
        x2_string = str(x2) + "000"
        int_string2 = str(int(x2)) if x2 >= 0 else "-" + str(int(x2))
        x2 = int_string2 + (x2_string[x2_string.index("."):x2_string.index(".") + 4])

        print("%s\n%s" % (x1, x2) if x1 < x2 else "%s\n%s" % (x2, x1))
    else:
        print("IMPOSSIBLE")
else:
    if b != 0:
        x = -c / b
        x_string = str(x) + "000"
        int_string = str(int(x)) if x >= 0 else "-" + str(int(x))
        x = int_string + (x_string[x_string.index("."):x_string.index(".") + 4])
        print("%s" % x)
    else:
        print("IMPOSSIBLE")
