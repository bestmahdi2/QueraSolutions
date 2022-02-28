# همه ی زیرمجموعه ها
# ID : 12912
# https://quera.org/problemset/12912/
# https://b2n.ir/e36183

from collections import deque

h = []

def printPowerSet(S, i, out=deque()):
    if i < 0:
        po = list(out)
        po.sort()
        h.append(po)
        return

    out.append(S[i])
    printPowerSet(S, i - 1, out)
    out.pop()

    while i > 0 and S[i] == S[i - 1]:
        i = i - 1

    printPowerSet(S, i - 1, out)


def findPowerSet(S):
    S.sort()
    printPowerSet(S, len(S) - 1)


haaayyyyy = int(input())
s = [int(u) for u in range(1, haaayyyyy + 1)]
printPowerSet(s, haaayyyyy - 1)
h.sort()

for k in h:
    st = str(k)
    st = st.replace("[", "{")
    st = st.replace("]", "}")
    print(st)

###########################################################

def sebSequence(number, step, keep, continuee):
    if step > number:
        return

    if continuee:
        printer(keep)

    keep.append(step + 1)
    sebSequence(number, step + 1, keep, True)

    keep.pop()
    sebSequence(number, step + 1, keep, False)


def printer(keep):
    temp = []
    for i in range(len(keep)):
        temp.append(keep[i])

    text = '{' + f'{", ".join([str(i) for i in temp])}' + '}'
    print(text)


number = int(input())
keep = []
sebSequence(number, 0, keep, True)
