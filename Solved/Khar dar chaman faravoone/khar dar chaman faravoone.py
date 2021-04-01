# خر در چمن فراوونه
# ID : 4065

number = (input()).split(" ")

a,b,l = int(number[0]), int(number[1]), int(number[2])

sums = 0
count = 1

while count <= l :
    if count%2 != 0:
        sums += a
    else:
        sums += b
    count += 1

print(sums)
