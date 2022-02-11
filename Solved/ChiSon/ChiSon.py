import json
n = int(input())
dict = {}
h = []
for i in range(n):
    c = input().split(" := ")
    if len(c) > 1:
        dict[c[0]] = json.loads(c[1])
    else:
        v = c[0].split("print ")
        v = v[1].split("[")
        v1 = v[1].split("]")
        v.pop(1)
        v.append(v1[0])
        h.append(dict[v[0]][json.loads(v[1])])
print(*h, sep="\n")
