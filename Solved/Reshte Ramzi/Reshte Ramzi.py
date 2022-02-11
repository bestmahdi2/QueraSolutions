# رشته‌ی رمزی
# ID : 106796
# https://quera.org/problemset/106796/
# https://b2n.ir/p38675

def lastToFirst(text):
    return text[-1] + text[:-1]


def replacer(text):
    result = []

    for i in text:
        if (i == 'z'):
            result.append('a')

        else:
            result.append(chr((ord(i) + 1)))

    return "".join(result)


length = input()
count = int(input())
text = input()

for i in range(count):
    a = lastToFirst(text)
    text = replacer(a)

print(text)
