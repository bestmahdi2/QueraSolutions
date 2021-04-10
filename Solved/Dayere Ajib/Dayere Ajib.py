# دایره عجیب
# ID : 34081
# https://quera.ir/problemset/contest/34081/%D8%B3%D8%A4%D8%A7%D9%84-%D8%B1%DB%8C%D8%A7%D8%B6%DB%8C%D8%A7%D8%AA-%D8%AF%D8%A7%DB%8C%D8%B1%D9%87-%D8%B9%D8%AC%DB%8C%D8%A8
# https://b2n.ir/s60073

n, k = [int(i) for i in input().split()]

turn = 1
count = 1
while True:
    turn += k
    turn = (turn - n) if turn > n else turn

    if turn == 1:
        break
    count += 1

print(count)
