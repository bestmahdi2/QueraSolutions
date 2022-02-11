# بسته در جدول
# ID : 106797
# https://quera.org/problemset/106797/
# https://b2n.ir/m78821

def isPrime(num):
    if num == 1:
        return False

    i = 2
    while i * i <= num:
        if num % i == 0:
            return False

        i += 1

    return True


def findCenter(num):
    return (num / 2) + 0.5


def findOpposite(length, num):
    center = findCenter(length)

    result = 0
    if length % 2 == 0:
        if num < center:
            result = int(center + (center - num))

        elif num > center:
            result = int(center - (num - center))

    else:
        if num == int(center):
            result = num

        elif num < center:
            result = int(center + (center - num))

        elif num > center:
            result = int(center - (num - center))

    return result


line = [int(i) for i in input().split(' ')]

row, column, count = line

keep = []

for i in range(row):
    inputer = input().split(' ')
    keep.append([])
    for j in range(column):
        keep[i].append(int(inputer[j]))

current = keep[0][0]
current_row = 0
current_column = 0

for i in range(count):
    if isPrime(current):
        current_row = findOpposite(row, current_row + 1) - 1
        current_column = findOpposite(column, current_column + 1) - 1
        current = keep[current_row][current_column]

    else:
        if current % 4 == 0:
            if current_column == column - 1:
                current_column = 0
            else:
                current_column += 1
            current = keep[current_row][current_column]

        elif current % 4 == 1:
            if current_row == row - 1:
                current_row = 0
            else:
                current_row += 1

            current = keep[current_row][current_column]

        elif current % 4 == 2:
            if current_column == 0:
                current_column = column - 1
            else:
                current_column -= 1

            current = keep[current_row][current_column]

        elif current % 4 == 3:
            if current_row == 0:
                current_row = row - 1
            else:
                current_row -= 1

            current = keep[current_row][current_column]

print(f'{current_row + 1} {current_column + 1}')
