# گزارش کار
# ID : 49535
# https://quera.ir/problemset/contest/49535/%D8%B3%D8%A4%D8%A7%D9%84-%D9%BE%DB%8C%D8%A7%D8%AF%D9%87-%D8%B3%D8%A7%D8%B2%DB%8C-%DA%AF%D8%B2%D8%A7%D8%B1%D8%B4-%DA%A9%D8%A7%D8%B1
# https://b2n.ir/j07770

n, k = [int(i) for i in input().split()]

sum = 0
for i in range(n):
    sum += int(input())

print("YES" if sum >= k else "NO")
