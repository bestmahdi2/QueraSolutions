# سری فیبوناتچی
# ID : ---
#
#

n = int(input())

jomle_sefrom = 0
jomle_yekom = 1

for i in range(n):
    adad = jomle_yekom + jomle_sefrom
    jomle_sefrom = jomle_yekom
    jomle_yekom = adad
print(jomle_sefrom)

###########################################################

n = int(input())

fibo = [1, 1]
for i in range(2, int(n)):
    fibo.append(fibo[i - 2] + fibo[i - 1])
print(fibo[int(n) - 1])

###########################################################

n = int(input())

jomle_sefrom, jomle_yekom = 0, 1
for _ in range(n):
    jomle_sefrom, jomle_yekom = jomle_yekom, jomle_yekom + jomle_sefrom
print(jomle_sefrom)
