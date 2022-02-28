# ساده تر
# ID : 3403
# https://quera.ir/problemset/contest/3403/%D8%B3%D8%A4%D8%A7%D9%84-%D8%B3%D8%A7%D8%AF%D9%87-%D8%AA%D8%B1
# https://b2n.ir/r02497

numbers = []
product = 1
for i in range(4):
    n = int(input())
    product *= n
    numbers.append(n)

print(f'Sum : {"%.6f" % sum(numbers)}')
print(f'Average : {"%.6f" % (sum(numbers) / 4)}')
print(f'Product : {"%.6f" % product}')
print(f'MAX : {"%.6f" % max(numbers)}')
print(f'MIN : {"%.6f" % min(numbers)}')

