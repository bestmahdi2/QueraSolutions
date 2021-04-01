# چاپ لوزی
# ID : 618

n = int(input())

for i in range(1, 2 * n + 2, 2):
    print(f'{" " * ((2 * n + 1 - i) // 2)}{"*" * i}')
for i in range(2 * n-1, 0, -2):
    print(f'{" " * ((2 * n + 1 - i) // 2)}{"*" * i}')
