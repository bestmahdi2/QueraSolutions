# رشته بلند
# ID : 66872
# https://quera.org/problemset/66872/
# https://b2n.ir/y43366


def copy(key, count):
    global suspiciousString
    text = key * count
    suspiciousString = text + suspiciousString[len(text):]


def compare(key):
    global suspiciousString
    global goodLevel
    if suspiciousString == key:
        goodLevel += 1


def substr(key, count):
    global suspiciousString
    global goodLevel
    if suspiciousString.count(key) == count:
        goodLevel += 1


def attach(key, count, str):
    global suspiciousString
    global goodLevel
    key += str
    if suspiciousString.count(key) == count:
        goodLevel += 1


def length(count):
    global suspiciousString
    global goodLevel
    if len(suspiciousString) == count:
        goodLevel += 1


def loop(inputer):
    global countCommand

    if inputer == "Is it right or not?":
        return

    inputer = inputer.split(" ")

    countCommand += 1

    if "copy" == inputer[0]:
        copy(key=inputer[1], count=int(inputer[2]))

    elif "compare" == inputer[0]:
        compare(key=inputer[1])

    elif "substr" == inputer[0]:
        substr(key=inputer[1], count=int(inputer[2]))

    elif "attach" == inputer[0]:
        attach(key=inputer[1], count=int(inputer[2]), str=inputer[3])

    elif "length" == inputer[0]:
        length(count=int(inputer[1]))

    loop(input())


goodLevel = 0
suspiciousString = input()
countCommand = 0

loop(input())

if goodLevel >= (countCommand // 2):
    print("Eyval")

else:
    print("HeifShod")
