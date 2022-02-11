import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/*
Question title = The Departed (2006)
https://quera.org/problemset/132251/
 */

public class TheDeparted {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<String> results = new ArrayList<>();

        for (int i = 1; i <= 5; i++) {
            String line = sc.nextLine();
            if (line.contains("FBI"))
                results.add(i + "");
        }

        if (results.size() == 0) {
            System.out.println("HE GOT AWAY!");
        } else {
            StringBuilder output = new StringBuilder();
            for (String i : results) {
                output.append(i).append(" ");
            }
            output.deleteCharAt(output.length() - 1);

            System.out.println(output.toString());
        }
    }
}