# نمایشگاه مجازی
# ID : 110015
# https://quera.org/problemset/110015/
# https://b2n.ir/z77955


count = int(input())
num = 1
remainingBooth = count

for i in range(1, 5):
    print("########.......########")

    if count == 1:
        print(f"#ghorfe{num}..............#")
        remainingBooth -= 1

    elif count == 0:
        print("#.....................#")

    else:
        print(f"#ghorfe{num}.......ghorfe{num + 1}#")
        remainingBooth -= 2
        num += 2

    count = remainingBooth

print("#######################")
