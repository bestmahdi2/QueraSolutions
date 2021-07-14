# در بند در ماندم
# ID : 6402
# https://quera.ir/problemset/contest/6402/%D8%B3%D8%A4%D8%A7%D9%84-%D8%AF%D8%B1-%D8%A8%D9%86%D8%AF-%D8%AF%D8%B1-%D9%85%D8%A7%D9%86%D8%AF%D9%85
# https://b2n.ir/b86165

n = int(input())
names = [input() for i in range(n)]


def darband(source, dest):
    main = f'{source} to {dest}: ke ba in dar agar dar bande dar manand, dar manand.'
    question = f'{dest} to {source}: dar manand?'
    answer = f'{source} to {dest}: dar manand.'

    print(main)
    print(question)
    if len(questions) > 0: print(*questions[::-1], sep="\n")
    if len(questions) > 0: print(*answers, sep="\n")
    print(answer)

    questions.append(question)
    answers.append(answer)


questions = []
answers = []
for i in range(n - 1):
    darband(names[i], names[i + 1])
