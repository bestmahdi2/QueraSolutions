# عدد خودمقلوب
# ID : 617
# https://quera.ir/problemset/university/617/%D8%B3%D8%A4%D8%A7%D9%84-%D8%AF%D8%A7%D9%86%D8%B4%DA%AF%D8%A7%D9%87-%D8%B5%D9%86%D8%B9%D8%AA%DB%8C-%D8%B4%D8%B1%DB%8C%D9%81-%D9%85%D8%A8%D8%A7%D9%86%DB%8C-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87%D9%86%D9%88%DB%8C%D8%B3%DB%8C-%D9%BE%D8%A7%DB%8C%DB%8C%D8%B2-%DB%B9%DB%B3-%D8%B9%D8%AF%D8%AF-%D8%AE%D9%88%D8%AF%D9%85%D9%82%D9%84%D9%88%D8%A8
# https://b2n.ir/932882

n = input()

if len(n) % 2 == 0:
    part1 = n[:len(n)//2]
    part2 = n[len(n)//2:]
else:
    part1 = n[:len(n)//2]
    part2 = n[len(n)//2 + 1:]

if part1 == part2[::-1]:
    print("YES")
else:
    print("NO")

###########################################################

n = input()

if len(n) % 2 == 0:
    part1 = n[:len(n)//2]
    part2 = n[len(n)//2:]
else:
    part1 = n[:len(n)//2]
    part2 = n[len(n)//2 + 1:]
x = 0
z = -1
while x < len(part1):
    if part1[x] == part2[z]:
        print("YES")
        break
    x += 1
    z -= 1
else:
    print("NO")

###########################################################

n = input()

print("YES" if n == n[::-1] else "NO")

###########################################################

n = input()

if n == n[::-1]:
    print("YES")
else:
    print("NO")
