t, w = map(int, input().split())
x = t * (2 ** (w-1))
y = (2 ** w) - 1
print("{:.4f}".format((float(round((x / y), 4)))))
