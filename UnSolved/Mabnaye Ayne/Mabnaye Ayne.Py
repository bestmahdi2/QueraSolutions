a, b, c = int(input()), int(input()), int(input())

def numberToBase(n, b):
    strings = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" #36 symbols

    if n == 0:
        return 0
    numbers = ""
    while n:
        numbers += strings[n % b]
        n //= b
    numbers = numbers[::-1]

    return "".join(numbers)

to_x = int(numberToBase(a, b))
n = str(numberToBase(c, to_x))
if n == n[::-1]:
    print("YES")
else:
    print("NO")


