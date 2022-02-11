# هندزفری ها
# ID : 110014
# https://quera.org/problemset/110014/
# https://b2n.ir/u60016

line1 = [i for i in input().split(" ")]
line2 = [i for i in input().split(" ")]

l1, r1 = line1
l2, r2 = line2

result = False
if l1 == r2 or l2 == r1 or l1 == r1 or l2 == r2:
    result = True

if result:
    print("YES")

else:
    print("NO")
