# رشته فیبوناچی
# ID : 17675
# https://quera.ir/problemset/contest/17675/%D8%B3%D8%A4%D8%A7%D9%84-%D8%B1%D8%B4%D8%AA%D9%87-%D9%81%DB%8C%D8%A8%D9%88%D9%86%D8%A7%DA%86%DB%8C
# https://b2n.ir/055190

n = int(input())

fibo = [1, 1]
for i in range(2, 11):
    fibo.append(fibo[i - 2] + fibo[i - 1])

keeper = []
for i in range(1, n + 1):
    if i in fibo:
        keeper.append("+")
    else:
        keeper.append("-")

print("".join(keeper))
