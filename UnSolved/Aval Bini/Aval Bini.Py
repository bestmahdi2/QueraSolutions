# اول بینی
# ID : 649
# https://quera.ir/problemset/university/649/%D8%B3%D8%A4%D8%A7%D9%84-%D8%AF%D8%A7%D9%86%D8%B4%DA%AF%D8%A7%D9%87-%D8%B5%D9%86%D8%B9%D8%AA%DB%8C-%D8%B4%D8%B1%DB%8C%D9%81-%D9%85%D8%A8%D8%A7%D9%86%DB%8C-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87%D9%86%D9%88%DB%8C%D8%B3%DB%8C-%D9%BE%D8%A7%DB%8C%DB%8C%D8%B2-%DB%B9%DB%B3-%D8%A7%D9%88%D9%84%D8%A8%DB%8C%D9%86%DB%8C
# https://b2n.ir/f91551

a, b = int(input()), int(input())
# lister = []
# if a < b:
#     for i in range(a+1, b):
#         for j in range(2, i//2):
#             if i % j == 0:
#                 break
#         else:
#             lister.append(str(i))
#     print(",".join(lister))
# else:
#     print(a)

result = ""
for i in range(a+1, b):
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count += 1

    if count == 2 and not result:
        result = str(i)
    elif count == 2:
        result += "," + str(i)

print(result)
