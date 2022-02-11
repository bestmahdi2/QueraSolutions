import java.util.Scanner;

/*
Question title = subasa va doostan - سوباسا و دوستان
https://quera.ir/problemset/108669/
 */

public class SoobasaVaDostan {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String[] input = sc.nextLine().split("\\s");
        int countGoal = Integer.parseInt(input[0]);
        int firstHalf = Integer.parseInt(input[1]);
        int secondHalf = Integer.parseInt(input[2]);

        String[] goals = sc.nextLine().split("\\s");

        int sum = calculate(goals, firstHalf, secondHalf);

        if (sum < countGoal)
            System.out.println("NO");
        else
            System.out.println("YES");
    }

    // returns sum of goals in first half and second half
    private static int calculate(String[] goals, int firstHalf, int secondHalf) {
        int firstTimeGoals = 0;
        int secondTimeGoals = 0;

        boolean done = false;
        int previousTimeInFirstHalf = Integer.parseInt(goals[0]);
        int previousTimeInSecondHalf = 45;

        for (String i : goals) {
            int goal = Integer.parseInt(i);

            // if the goal is in the first half
            if (goal <= 45 + firstHalf && goal >= previousTimeInFirstHalf && !done) {
                firstTimeGoals++;
            }
            // if the goal is in the second half
            else if (goal >= 45 && goal <= 90 + secondHalf && goal >= previousTimeInSecondHalf) {
                secondTimeGoals++;
                done = true;
                previousTimeInSecondHalf = goal;
            }
            previousTimeInFirstHalf = goal;
        }
        return firstTimeGoals + secondTimeGoals;
    }
}