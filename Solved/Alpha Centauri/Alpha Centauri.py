# آلفا قنطورس
# ID : 66859
# https://quera.org/problemset/66859/
# https://b2n.ir/d99346


def NumberToChar(number):
    if 0 <= number <= 9:
        return chr(ord('0') + number)

    else:
        return chr(ord('A') + number - 10)


def baseConverter(keeper, number, base):
    if base == 10:
        return str(number)

    else:
        while True:
            if number > 0:
                keeper += NumberToChar(number % base)
                number = int(number / base)
            else:
                break

        return keeper[::-1]


n, b = input().split(" ")
print(baseConverter(keeper="", number=int(n), base=int(b)))
