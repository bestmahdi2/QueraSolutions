# بهداشت و سلامت
# ID : 51865
# https://quera.ir/problemset/contest/51865/%D8%B3%D8%A4%D8%A7%D9%84-%D9%BE%DB%8C%D8%A7%D8%AF%D9%87-%D8%B3%D8%A7%D8%B2%DB%8C-%D8%A8%D9%87%D8%AF%D8%A7%D8%B4%D8%AA-%D9%88-%D8%B3%D9%84%D8%A7%D9%85%D8%AA
# https://b2n.ir/064854

score = int(input())
days = int(input())

if days == 0:
    print(20)
elif days == 7:
    print(score)
else:
    print(score - days if (score - days) > 0 else 0)
