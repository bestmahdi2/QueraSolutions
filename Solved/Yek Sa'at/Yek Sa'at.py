# یک ساعت
# ID : 2886
# https://quera.ir/problemset/contest/2886/%D8%B3%D8%A4%D8%A7%D9%84-%DB%8C%DA%A9-%D8%B3%D8%A7%D8%B9%D8%AA
# https://b2n.ir/y36493

hour, min = [int(i) for i in input().split()]
min = "00" if min == 0 else str(60 - min)
hour = "00" if hour == 0 else str(12 - hour)

if len(min) < 2:
    min = "0" + min

if len(hour) < 2:
    hour = "0" + hour

print(f'{hour}:{min}')
