# آخ جون طرف نیست!
# ID : 3538
# https://quera.ir/problemset/contest/3538/%D8%B3%D8%A4%D8%A7%D9%84-%D8%A2%D8%AE-%D8%AC%D9%88%D9%86-%D8%B7%D8%B1%D9%81-%D9%86%DB%8C%D8%B3%D8%AA
# https://b2n.ir/s82371

n1 = input()
string1 = input().split()
n2 = input()
string2 = input().split()
n3 = input()
string3 = input().split()

days = ["shanbe", "1shanbe", "2shanbe", "3shanbe", "4shanbe", "5shanbe", "jome"]
for string in [string1, string2, string3]:
    for i in string:
        if i in days:
            days.remove(i)
print(len(days))
