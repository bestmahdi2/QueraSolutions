# خُب باقر سرما خورده
# ID : 10231
# https://quera.ir/problemset/contest/10231/%D8%B3%D8%A4%D8%A7%D9%84-%D8%AE%D8%A8-%D8%A8%D8%A7%D9%82%D8%B1-%D8%B3%D8%B1%D9%85%D8%A7-%D8%AE%D9%88%D8%B1%D8%AF%D9%87
# https://b2n.ir/e33907

numbers = []
for i in range(5):
    string = input()
    if "MOLANA" in string or "HAFEZ" in string:
        numbers.append(str(i + 1))
print(" ".join(numbers) if len(numbers) else "NOT FOUND!")

###########################################################
