# تکرار حرف در رشته
# ID : ---
#
#


voroodi = input()

kalame = voroodi[:-2]
character = voroodi[-1:]

tedad = len(kalame)
for harf in kalame:
    if harf != character:
        tedad -= 1

print(tedad)

###########################################################

voroodi = input()

input_list = voroodi.split(" ")
kalame = input_list[0]
character = input_list[1]

tedad = 0
x = 0
while x < len(kalame):
    if kalame[x] == character:
        tedad += 1
    x += 1

print(tedad)

###########################################################

voroodi = input()

x = 0
for i in voroodi:
    if i == " ":
        index_space = 1
        break
    x += 1
kalame = voroodi[:x]
character = voroodi[x+1:]

tedad = 0
for i in range(len(kalame)):
    if kalame[i] == character:
        tedad += 1

print(tedad)

###########################################################

voroodi = input()

kalame = voroodi[:voroodi.index(" ")]
character = voroodi[voroodi.index(" ") + 1:]

tedad = 0
for harf in kalame:
    if harf == character:
        tedad += 1

print(tedad)
