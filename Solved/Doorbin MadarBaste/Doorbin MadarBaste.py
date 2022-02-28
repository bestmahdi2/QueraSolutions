# دوربین مداربسته
# ID : 2794
# https://quera.ir/problemset/contest/2794/%D8%B3%D8%A4%D8%A7%D9%84-%D8%AF%D9%88%D8%B1%D8%A8%DB%8C%D9%86-%D9%85%D8%AF%D8%A7%D8%B1%D8%A8%D8%B3%D8%AA%D9%87
# https://b2n.ir/771462

a = input().split()
b = input().split()
c = input().split()

d1 = [a[0], b[0], c[0]]
d1 = [i for i in set(d1) if d1.count(i) == 1]
d2 = [a[1], b[1], c[1]]
d2 = [i for i in set(d2) if d2.count(i) == 1]

print(d1[0], d2[0])
