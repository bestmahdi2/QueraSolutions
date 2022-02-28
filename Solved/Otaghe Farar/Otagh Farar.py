# اتاق فرار
# ID : 123801
# https://quera.org/problemset/123801/
# https://b2n.ir/a16684


a = list(map(int, input().split()))
b = list(map(int, input().split()))


def hi(ls, sl):
    res1 = str(ls[0] + sl[0])
    res2 = str(ls[1] + sl[1])
    res3 = str(ls[2] + sl[2])
    ress = (res1[-1]) + (res2[-1]) + (res3[-1])
    ress = int(ress)

    if ress % 6 == 0:
        return "Boro joloo :)"

    else:
        return "Gir oftadi :("


counter = 0
for i in range(len(a)):
    win = 0
    loose = 0
    r = a.pop(0)
    a.append(r)

    for j in range(len(a)):
        counter += 1
        r2 = b.pop(0)
        b.append(r2)
        q = hi(a, b)
        if q == "Boro joloo :)":
            win += 1
            break
        else:
            if counter == 25:
                loose += 1
                break

    if win != 0:
        print("Boro joloo :)")
        break

    elif loose != 0:
        print("Gir oftadi :(")
        break
