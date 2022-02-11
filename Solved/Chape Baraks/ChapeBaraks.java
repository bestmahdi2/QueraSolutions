import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

/*
Question title = chap barax - چاپ برعکس
https://quera.ir/problemset/3405/
 */

public class ChapeBaraks {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<String> list = new ArrayList<>();
        while (true) {
            String input = sc.nextLine().trim();
            if (input.equals("0")) {
                break;
            } else {
                list.add(input);
            }
        }
        Collections.reverse(list);
        for (String i : list) {
            System.out.println(i);
        }
    }
}