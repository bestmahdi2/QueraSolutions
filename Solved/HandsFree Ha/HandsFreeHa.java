import java.util.Scanner;

/*
Question title = handsfree ha - هندزفری‌ها
https://quera.ir/problemset/110014/
 */

public class HandsFreeHa {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] line1 = sc.nextLine().trim().split("\\W");
        String[] line2 = sc.nextLine().trim().split("\\W");

        String l1 = line1[0];
        String r1 = line1[1];
        String l2 = line2[0];
        String r2 = line2[1];

        boolean result = false;
        if (l1.equals(r2) || l2.equals(r1) || l1.equals(r1) || l2.equals(r2)) {
            result = true;
        }
        if (result)
            System.out.println("YES");
        else
            System.out.println("NO");
    }
}