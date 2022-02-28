# تَخَطّی‌گَری
# ID : 129728
# https://quera.org/problemset/129728/
# https://b2n.ir/b32744

print(*sorted([i.lower() if (ord(i) - 97) % 2 == 0 else i.upper() for i in input()], reverse=True))
