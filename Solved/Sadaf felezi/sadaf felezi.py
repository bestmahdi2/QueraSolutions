# صدف فلزی
# ID : 6581
# https://quera.org/problemset/6581/
# https://b2n.ir/x03715

t, w = map(int, input().split())
x = t * (2 ** (w-1))
y = (2 ** w) - 1

print("{:.4f}".format((float(round((x / y), 4)))))