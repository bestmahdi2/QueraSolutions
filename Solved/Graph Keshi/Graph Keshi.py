#ID : 66866
#https://quera.org/problemset/66866/

#score : 94
#The time limit exceeds the asked time limit in ony one question

n = int(input())
nums = list(map(int, input().split()))
nums.sort()
count=0
melak = 0
for i in range(n):
    for j in range(i+1, n):
        melak = nums[j] - nums[i]
        if (melak) > 1:
            break
        elif (melak) == 1:
            count += 1
print(count)
