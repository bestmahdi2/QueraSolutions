# تو چقدر اضافه وزن داری؟
# ID : 3404
# https://quera.ir/problemset/contest/3404/%D8%B3%D8%A4%D8%A7%D9%84-%D8%AA%D9%88-%DA%86%D9%82%D8%AF%D8%B1-%D8%A7%D8%B6%D8%A7%D9%81%D9%87-%D9%88%D8%B2%D9%86-%D8%AF%D8%A7%D8%B1%DB%8C
# https://b2n.ir/785885

weight = float(input())
height = float(input())

bmi = weight/(height ** 2)

print("%.2f" % bmi)
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")

###########################################################
