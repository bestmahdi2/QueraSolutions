# تست بینایی
# ID : 2659
# https://quera.ir/problemset/contest/2659/%D8%B3%D8%A4%D8%A7%D9%84-%D8%AA%D8%B3%D8%AA-%D8%A8%DB%8C%D9%86%D8%A7%DB%8C%DB%8C
# https://b2n.ir/997305

letters = int(input())
original = input()
student = input()

number = 0

for i in range(letters):
    if original[i] != student[i]:
        number += 1
print(number)
