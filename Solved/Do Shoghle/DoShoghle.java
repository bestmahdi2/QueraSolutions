import java.util.Scanner;

/*
Question title = do shoghle - دو شغله
https://quera.ir/problemset/111990/
 */

public class DoShoghle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String day = sc.nextLine();

        int num = 0;
        if ("shanbe".equals(day) || "doshanbe".equals(day) || "chaharshanbe".equals(day)) {
            num = 2;
        } else if ("yekshanbe".equals(day) || "panjshanbe".equals(day) || "seshanbe".equals(day)) {
            num = 1;
        } else if ("jome".equals(day)) {
            num = -1;
        }
        if (num > 0) {
            if (num % 2 == 0)
                System.out.println("perspolis");
            else
                System.out.println("bahman");
        } else {
            System.out.println("tatil");
        }
    }
}