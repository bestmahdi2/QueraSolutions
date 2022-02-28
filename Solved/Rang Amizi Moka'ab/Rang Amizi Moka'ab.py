# رنگ‌آمیزی مکعب - پایتون
# ID : 33034
# https://quera.org/problemset/33034/
# https://b2n.ir/f61591

def coloring(h):
    h = list(h)
    counter = 0

    for k in h:
        counter2 = 0
        if counter == 0 or counter == (len(h) - 1):
            for k2 in k:
                for k3 in range(len(k2)):
                    k2[k3] = 1

        else:
            for k2 in k:
                for k3 in range(len(k2)):
                    if counter2 == 0 or counter2 == (len(k) - 1):
                        k2[k3] = 1
                    else:
                        if k3 == 0 or k3 == (len(k2) - 1):
                            k2[k3] = 1
                        else:
                            k2[k3] = 0
                counter2 += 1

        counter += 1

    return (h)
