# بازی تفاضل
# ID : 87176
# https://quera.org/problemset/87176/
# https://b2n.ir/m87131

def game(number):
    strNumber = str(number)

    if (strNumber[1] > strNumber[0]):
        result = int(strNumber[1]) - int(strNumber[0])

    else:
        result = int(strNumber[0]) - int(strNumber[1])

    return result
