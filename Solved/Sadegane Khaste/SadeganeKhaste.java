import java.util.*;

/*
Question title = Sadgane khaste - صدگان خسته
https://quera.ir/problemset/3406/
 */

public class SadeganeKhaste {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String strInput = sc.nextLine();
        String strInput2 = sc.nextLine();
        char[] input1 = strInput.toCharArray();
        char[] input2 = strInput2.toCharArray();
        List<Character> list = new ArrayList<>();
        List<Character> list2 = new ArrayList<>();

        for (char i : input1) {
            list.add(i);
        }
        for (char i : input2) {
            list2.add(i);
        }

        Collections.reverse(list);
        Collections.reverse(list2);
        int num1 = toString(list);
        int num2 = toString(list2);

        if (num1 > num2) {
            System.out.println(strInput2 + " < " + strInput);
        } else if (num1 < num2)
            System.out.println(strInput + " < " + strInput2);
        else {
            System.out.println(strInput + " = " + strInput2);
        }
    }

    private static int toString(List<Character> list) {
        StringBuilder sb = new StringBuilder();
        for (char i : list) {
            sb.append(i);
        }
        return Integer.parseInt(sb.toString());
    }
}