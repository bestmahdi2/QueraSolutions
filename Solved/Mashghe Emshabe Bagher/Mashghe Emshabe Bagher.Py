# مشق امشب باقر
# ID : 10230

i = input()
if "0" not in i.split(" "):
    if sum([int(j) for j in i.split(" ")]) == 180:
        print("Yes")
    else:
        print("No")
else:
    print("No")
