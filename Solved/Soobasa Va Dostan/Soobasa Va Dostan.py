# سوباسا و دوستان
# ID : 108669
# https://quera.org/problemset/108669/
# https://b2n.ir/u73922

def calculate(goals, firstHalf, secondHalf):
    firstTimeGoals = 0
    secondTimeGoals = 0

    done = False
    previous_time_in_first_half = int(goals[0])
    previous_time_in_second_half = 45

    for i in goals:
        goal = int(i)

        if 45 + firstHalf >= goal >= previous_time_in_first_half and not done:
            firstTimeGoals += 1

        elif 45 <= goal <= 90 + secondHalf and goal >= previous_time_in_second_half:
            secondTimeGoals += 1
            done = True
            previous_time_in_second_half = goal

        previous_time_in_first_half = goal

    return firstTimeGoals + secondTimeGoals


inputer = [int(i) for i in input().split(" ")]
countGoal, firstHalf, secondHalf = inputer
goals = input().split(" ")

sum = calculate(goals, firstHalf, secondHalf)

if sum < countGoal:
    print("NO")

else:
    print("YES")
