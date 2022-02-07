# رژیم سخت
# ID : 20256
# https://quera.ir/problemset/contest/20256/%D8%B3%D8%A4%D8%A7%D9%84-%D8%B1%DA%98%DB%8C%D9%85-%D8%B3%D8%AE%D8%AA
# https://b2n.ir/t20497

string = input()
if string.count("R") >= 3:
    print("nakhor lite")

elif string.count("R") >= 2 and string.count("Y") >= 2:
    print("nakhor lite")

elif string.count("G") == 0:
    print("nakhor lite")

else:
    print("rahat baash")
