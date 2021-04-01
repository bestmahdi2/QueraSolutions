# تک رقمی
# ID : 3539

i = input()
while len(i) > 1:
    i = str(sum([int(j) for j in i]))
print(int(i))
