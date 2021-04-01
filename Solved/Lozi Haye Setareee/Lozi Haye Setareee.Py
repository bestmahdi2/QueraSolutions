# لوزی های ستاره ای
# ID : 9773

n = int(input())

for i in range(1, n + 1, 2):
    print(f'{" " * ((n - i) // 2)}{"*" * i}{" " * (n - i -1)}{"*" * i}')
for i in range(n-2, 0, -2):
    print(f'{" " * ((n - i) // 2)}{"*" * i}{" " * (n - i - 1)}{"*" * i}')
