import java.util.Scanner;

public class HendooneKhori {

    static Scanner scanner;

    public static void main(String[] args) {
        int i;
        // melon count
        scanner = new Scanner(System.in);
        int n = Integer.parseInt(scanner.nextLine());
        if (n < 1)
            n = 1;

        // weight
        String weightText = scanner.nextLine();
        String[] weightTextArray = weightText.split(" ");

        int s1 = 0;
        int s2 = 1;
        int sNext = 2;
        int min = 0;

        for (i = 0; i < n - 1; i++) {
            min = Math.min(Integer.parseInt(weightTextArray[s1]), Integer.parseInt(weightTextArray[s2]));
            if (min == Integer.parseInt(weightTextArray[s1])) {
                weightTextArray[s1] = "-1";
                s1 = sNext;
                sNext++;
            } else if (min == Integer.parseInt(weightTextArray[s2])) {
                weightTextArray[s2] = "-1";
                s2 = sNext;
                sNext++;
            }

        }
        for (i = 0; i < n; i++)
            if (!weightTextArray[i].equals("-1")) {
                System.out.println(i + 1);
                break;
            }

    }

}