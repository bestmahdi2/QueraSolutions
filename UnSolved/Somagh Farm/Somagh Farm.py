# سماق فارم
# ID : 66865
# https://quera.org/problemset/66865/
# https://b2n.ir/z39526

a = int(input())
b = [int(o) for o in input().split()]

sortBig = b.copy()
sortBig.sort()
sortSml = b.copy()
sortSml.sort()
sortSml = sortSml[::-1]

if b == sortBig or b == sortSml:
    print("Yes")

else:
    hay = 0
    for i in range(1, a - 1):
        list1 = b[:i]
        list2 = b[i + 1:]
        list1CB = list1.copy()
        list1CB.sort()
        list2CB = list2.copy()
        list2CB.sort()
        list2CB = list2CB[::-1]

        list1CK = list1.copy()
        list1CK.sort()
        list1CK = list1CK[::-1]
        list2CK = list2.copy()
        list2CK.sort()

        if b[i] > list1[-1] and b[i] >= list2[0]:
            if list1 == list1CB and list2 == list2CB:
                print("Yes")
                hay += 1
                break

        elif b[i] < list1[-1] and b[i] < list2[0]:
            if list1 == list1CK and list2 == list2CK:
                print("Yes")
                hay += 1
                break

    if hay == 0:
        print("No")
