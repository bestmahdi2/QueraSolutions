import java.util.Scanner;

/*
Question title = baste dar jadval - بسته در جدول
https://quera.ir/problemset/106797/
 */
public class BasteDarJadval {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();

        int row = Integer.parseInt(line.split("\\s")[0]);
        int column = Integer.parseInt(line.split("\\s")[1]);
        int count = Integer.parseInt(line.split("\\s")[2]);

        int[][] list = new int[row][column];

        //getting table values from user
        for (int i = 0; i <= row - 1; i++) {
            String input = sc.nextLine();
            for (int j = 0; j <= column - 1; j++) {
                list[i][j] = Integer.parseInt(input.split("\\s")[j]);
            }
        }
        //current value
        int current = list[0][0];
        //current row index
        int currentRow = 0;
        //current column index
        int currentColumn = 0;

        for (int i = 0; i <= count - 1; i++) {
            //if current number is prime , than go to opposite row and column
            if (isPrime(current)) {
                currentRow = findOpposite(row, currentRow + 1) - 1;
                currentColumn = findOpposite(column, currentColumn + 1) - 1;
                current = list[currentRow][currentColumn];

            } else {
                switch (current % 4) {
                    case 0:
                        if (currentColumn == column - 1) {
                            currentColumn = 0;
                        } else {
                            currentColumn++;
                        }
                        current = list[currentRow][currentColumn];
                        break;
                    case 1:
                        if (currentRow == row - 1) {
                            currentRow = 0;
                        } else {
                            currentRow++;
                        }
                        current = list[currentRow][currentColumn];

                        break;
                    case 2:
                        if (currentColumn == 0) {
                            currentColumn = column - 1;
                        } else {
                            currentColumn--;
                        }
                        current = list[currentRow][currentColumn];

                        break;
                    case 3:
                        if (currentRow == 0) {
                            currentRow = row - 1;
                        } else {
                            currentRow--;
                        }
                        current = list[currentRow][currentColumn];
                        break;
                }
            }
        }
        System.out.println(currentRow + 1 + " " + (currentColumn + 1));
    }

    //check if a number is prime or not
    private static boolean isPrime(int num) {
        boolean isPrime = true;
        for (int i = 2; i <= num / 2 + 1; i++) {
            if (num % i == 0) {
                isPrime = false;
                break;
            }
        }
        return isPrime;
    }

    //returns middle cell in given table length
    private static double findCenter(int num) {

        return (num / 2.0) + 0.5;
    }

    //returns opposite cell in given row or column
    private static int findOpposite(int length, int num) {
        double center = findCenter(length);
        //even
        int result = 0;
        if (length % 2 == 0) {
            if (num < center) {
                result = (int) (center + (center - num));
            }
            if (num > center) {
                result = (int) (center - (num - center));
            }
        }
        //odd
        else {
            if (num == (int) center) {
                result = num;
            }
            if (num < center) {
                result = (int) (center + (center - num));
            }
            if (num > center) {
                result = (int) (center - (num - center));
            }
        }
        return result;
    }
}