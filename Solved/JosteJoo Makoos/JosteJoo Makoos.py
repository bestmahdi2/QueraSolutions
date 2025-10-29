# جستوجوی معکوس
# ID : 632
# https://quera.org/problemset/632/
# https://b2n.ir/s86937

import re
sentence = input()
word = input()
sentence = sentence.lower()
word = word.lower()
word = word.strip()
reverse = word[::-1]
tokens = re.findall(r'\w+|[^\w\s]', sentence)
result = 0
for i in tokens:
    if word == i:
        result += 1
if word == reverse:
    print(result)
else:
    for i in tokens:
        if reverse == i:
            result += 1
    print(result)




