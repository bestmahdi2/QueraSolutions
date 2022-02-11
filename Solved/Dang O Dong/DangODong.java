import java.util.Scanner;

/*
Question title = Dang va Dong - دَنگ و دُنگ
https://quera.ir/problemset/127290/
 */

public class DangODong {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int rows = Integer.parseInt(sc.nextLine());
        StringBuilder result = new StringBuilder();
        for (int i = 1; i <= rows; i++) {

            String[] line = sc.nextLine().split("\\s");
            result.append(result(line)).append("\n");

        }
        System.out.println(result.toString());
    }

    private static String result(String[] line) {
        int people = Integer.parseInt(line[0]);
        int paidMoney = Integer.parseInt(line[1]);
        int fee = Integer.parseInt(line[2]);

        int paidPerPerson = (paidMoney - fee) / people;
        if (paidPerPerson <= 0) {
            return "-1";
        }
        int paidByPayer = paidMoney - ((people - 1) * paidPerPerson);
        int paidPerPersonWithFee = paidPerPerson + fee;
        if (paidByPayer == paidPerPersonWithFee)
            return paidPerPerson + "";
        else
            return "-1";
    }
}