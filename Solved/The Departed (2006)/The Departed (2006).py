h = []
for i in range(1, 6):
    a = input()
    if "FBI" in a:
        h.append(i)
if len(h) > 0:
    print(*h, sep=" ")
else:
    print("HE GOT AWAY!")
