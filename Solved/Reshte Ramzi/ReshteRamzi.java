import java.util.Scanner;

/*
Question title = reshte ramzi - رشته رمزی
https://quera.ir/problemset/106796/
 */

public class ReshteRamzi {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String length = sc.nextLine();
        int count = Integer.parseInt(sc.nextLine());
        String text = sc.nextLine();

        for (int i = 0; i <= count - 1; i++) {
            String a = lastToFirst(text);
            text = replace(a);
        }
        System.out.println(text);
    }

    //move last letter to first
    private static String lastToFirst(String text) {
        char l = text.charAt(text.length() - 1);
        StringBuilder builder = new StringBuilder(text);
        builder.deleteCharAt(text.length() - 1);
        return l + builder.toString();
    }

    //replace all letters with their next letter in alphabet
    private static String replace(String text) {
        StringBuilder result = new StringBuilder();
        for (char i : text.toCharArray()) {
            if (i == 'z') {
                result.append('a');
            } else {
                result.append((char) (((int) i) + 1));
            }
        }
        return result.toString();
    }
}