# تعمیر دیوار
# ID : 6580
# https://quera.org/problemset/6580/
# https://b2n.ir/h42729

x, y = input().split()
n = int(input())
dx, dy = input().split()

fx = int(x) + n
fy = int(y) - n

if int(x) <= int(dx) <= int(fx) and int(y) >= int(dy) >= int(fy):
    print("Mahdi")

else:
    print("Parsa")
