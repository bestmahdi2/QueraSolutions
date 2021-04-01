# همایش زندگی بهتر
# ID : 10325

i = [int(j) for j in input().split(" ")]
if i[1] <= 10:
    print(f'Right {11 - i[0]} {i[1]}')
else:
    print(f'Left {11 - i[0]} {21 - i[1]}')
