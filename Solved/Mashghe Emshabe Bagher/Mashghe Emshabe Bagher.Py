# مشق امشب باقر
# ID : 10230
# https://quera.ir/problemset/contest/10230/%D8%B3%D8%A4%D8%A7%D9%84-%D9%85%D8%B4%D9%82-%D8%A7%D9%85%D8%B4%D8%A8-%D8%A8%D8%A7%D9%82%D8%B1
# https://b2n.ir/y28651

i = input()
if "0" not in i.split(" "):
    if sum([int(j) for j in i.split(" ")]) == 180:
        print("Yes")
    else:
        print("No")
else:
    print("No")

###########################################################
