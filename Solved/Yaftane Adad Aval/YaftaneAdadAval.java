import java.util.Scanner;

/*
Question title = yaftan adad aval - یافتن عدد اول
https://quera.ir/problemset/593/
 */

public class YaftaneAdadAval {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();

        int sumDigits = sumDigits(num);
        int i = num + 1;
        int primeCounter = 0;
        int prime = 0;
        while (primeCounter != sumDigits) {
            if (isPrime(i)) {
                primeCounter++;
                prime = i;
                i++;
            } else
                i++;

        }
        System.out.println(prime);
    }

    private static int sumDigits(int num) {
        char[] chars = (num + "").toCharArray();
        int result = 0;
        for (char i : chars) {
            result += Integer.parseInt(i + "");
        }
        return result;
    }

    private static boolean isPrime(int num) {
        int counter = 0;
        for (int j = 2; j <= num - 1; j++) {
            if (num % j == 0) {
                counter++;
            }
        }
        return counter == 0;
    }
}